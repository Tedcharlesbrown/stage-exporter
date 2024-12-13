from prometheus_client import Gauge, REGISTRY
from functions import validize_name, get_request
from API.Brompton_Tessera.api import endpoints

DEBUG = False

METRICS = {}
METRIC_PREFIX = "tessera_"

model_ports = [
	{"model": "sx40", "sdi-port": 1, "hdmi-port": 1},
	{"model": "gen3", "sdi-port": 4, "hdmi-port": 4, "dp-port": 4},
]

def uptime_to_seconds(uptime):
	"""
	Incoming String = '88d 1195h 71608s'
	Takes the Seconds and outputs int
	"""
	for part in uptime.split():
		if part.endswith("s"):
			return int(part[:-1])

# Preprocess the endpoints based on processor type and available ports
def preprocess_endpoints(processor_type):
	filtered_endpoints = []
	for endpoint in endpoints:
		path = endpoint["path"]
		
		# Skip endpoints
		if (endpoint["type"] == "string" or endpoint["type"] == "bytearray" or endpoint["type"] == "array") and path != "api/system/uptime":
			if DEBUG: print(f"Skipping string endpoint: {path}")
			continue
		if path == "api/override/test-pattern/frame-store/capture-frame" or path == "api/override/test-pattern/frame-store/delete-frame":
			if DEBUG: print(f"Skipping endpoint: {path}")
			continue

		# Port Numbers and Placeholders
		if "{" in path:  # Check for placeholders
			for port_type in ["dvi-port-number", "sdi-port-number", "hdmi-port-number", "dp-port-number"]:
				base_port_type = port_type.replace("-number", "")  # Extract base type (e.g., "hdmi-port")
				if f"{{{port_type}}}" in path:
					# Find the model data matching the processor type
					model_data = next((m for m in model_ports if m["model"] == processor_type), None)
					if model_data and base_port_type in model_data:
						port_count = model_data[base_port_type]
						# Generate endpoints for each port index
						for i in range(port_count):
							new_path = path.replace(f"{{{port_type}}}", str(i))
							filtered_endpoints.append({**endpoint, "path": new_path})
					else:
						# Skip the endpoint if the port is not available
						if DEBUG: print(f"Skipping {path} for {port_type} as it's not available in the model.")
						break
		else:
			filtered_endpoints.append(endpoint)  # Add endpoint without placeholders
	
	if DEBUG: print(f"Filtered Endpoints: {filtered_endpoints}")
	return filtered_endpoints


def initialize_metrics(processor_type):
	filtered_endpoints = preprocess_endpoints(processor_type)
	for endpoint in filtered_endpoints:
		description = endpoint['description']
		if 'range' in endpoint:
			description += f" RANGE: {endpoint['range']}"
		if 'supported_values' in endpoint:
			description += f" Supported values: {endpoint['supported_values']}"
		
		metric_name = f"{METRIC_PREFIX}{validize_name(endpoint['path'])}"
		if metric_name not in REGISTRY._names_to_collectors:
			# Use the description as the `help` text
			METRICS[endpoint['path']] = Gauge(
				metric_name,
				description,  # This `description` is used for the tooltip in Grafana
				["source"]  # Label for identifying the source
			)
	return filtered_endpoints


def collect_metrics(target, label):
	ip, port = target.split(":")
	processor_type = get_request(ip, port, "api/system/processor-type").get("processor-type", None)
	filtered_endpoints = initialize_metrics(processor_type)
	for endpoint in filtered_endpoints:
		path = endpoint["path"]
		try:
			response = get_request(ip, port, path)
			if DEBUG: print("Raw Response:", response)  # Debug: Print the raw API response
			if response is not None:
				response_key = path.split("/")[-1]
				value = response.get(response_key, None)
				if value is not None:
					if endpoint["type"] == "string":
						METRICS[path].labels(source=value).set(1)
					if endpoint["type"] == "enum":
						if value in endpoint["supported_values"]:
							index = endpoint["supported_values"].index(value)
							METRICS[path].labels(source=label).set(index)
						else:
							if DEBUG: print(f"Unsupported enum value: {value}. Supported values: {endpoint['supported_values']}")
					elif endpoint["path"] == "api/system/uptime":
						uptime_seconds = uptime_to_seconds(value)
						METRICS[path].labels(source=label).set(uptime_seconds)
					elif endpoint["type"] == "bool":
						boolean_value = 1 if value else 0
						METRICS[path].labels(source=label).set(boolean_value)
					elif endpoint["type"] in ["int", "float"]:
						METRICS[path].labels(source=label).set(value)
					else:
						print(f"Unsupported type for {path}: {endpoint['type']}")
				else:
					print(f"Response missing expected key '{response_key}' for path {path}.")
			else:
				print(f"Empty response for path {path} from target {target}.")
		except Exception as e:
			print(f"Failed to fetch or set metric for {path}: {e}")

	# Sort metrics alphabetically by source label
	for metric_name, metric in METRICS.items():
		if hasattr(metric, '_metrics'):
			metric._metrics = {
				k: v for k, v in sorted(metric._metrics.items(), key=lambda item: item[0][0])
			}