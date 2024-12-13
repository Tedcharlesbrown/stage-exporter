from prometheus_client import Gauge, REGISTRY
from functions import validize_name, get_request
from API.Disguise.api import endpoints

DEBUG = False

METRICS = {}
METRIC_PREFIX = "disguise_"

# Recursively extract numeric fields from a nested dictionary
def extract_numeric_fields(data, path=""):
	numeric_paths = []
	if isinstance(data, dict):
		for key, value in data.items():
			current_path = f"{path}/{key}" if path else key
			if isinstance(value, dict):
				numeric_paths.extend(extract_numeric_fields(value, current_path))
			elif isinstance(value, list):
				for index, item in enumerate(value):
					current_indexed_path = f"{current_path}[{index}]"
					numeric_paths.extend(extract_numeric_fields(item, current_indexed_path))
			elif value in ["int", "float"]:
				numeric_paths.append(current_path)
	return numeric_paths

# Preprocess the endpoints to find numeric return fields
def preprocess_endpoints():
	filtered_endpoints = []
	for endpoint in endpoints:
		if 'returns' in endpoint:
			numeric_fields = extract_numeric_fields(endpoint['returns'])
			if numeric_fields:
				filtered_endpoints.append({"endpoint": endpoint, "numeric_fields": numeric_fields})
		else:
			if DEBUG: print(f"Skipping endpoint without numeric returns: {endpoint['path']}")
			continue

	if DEBUG: print(f"Filtered Disguise Endpoints: {filtered_endpoints}")
	return filtered_endpoints

def initialize_metrics():
	filtered_endpoints = preprocess_endpoints()
	for item in filtered_endpoints:
		endpoint = item['endpoint']
		for field in item['numeric_fields']:
			description = f"{endpoint['description']} - Field: {field}"
			raw_metric_key = f"{endpoint['path']}/{field}"
			metric_key = validize_name(raw_metric_key)
			metric_name = f"{METRIC_PREFIX}{validize_name(endpoint['path'])}_{validize_name(field)}"
			if DEBUG: print(f"Initializing metric {metric_name} with key {metric_key}")
			if metric_name not in REGISTRY._names_to_collectors:
				METRICS[metric_key] = Gauge(
					metric_name,
					description,
					["source"]
				)
	if DEBUG: print(f"Initialized Metrics: {METRICS.keys()}")
	return filtered_endpoints

def collect_metrics(target, label):
	ip, port = target.split(":")
	filtered_endpoints = initialize_metrics()
	for item in filtered_endpoints:
		endpoint = item['endpoint']
		path = endpoint['path']
		try:
			response = get_request(ip, port, path)
			if DEBUG: print(f"Raw Response for {path}: {response}")
			if response is not None:
				for field in item['numeric_fields']:
					field_parts = field.split('/')
					value = response
					try:
						for part in field_parts:
							if '[' in part and ']' in part:  # Handle indexed fields
								key, index = part[:-1].split('[')
								index = int(index)
								if isinstance(value, dict) and key in value and isinstance(value[key], list):
									value = value[key][index]
								else:
									raise KeyError(f"Key {key} with index {index} not found or not a list.")
							else:
								if isinstance(value, dict) and part in value:
									value = value[part]
								elif isinstance(value, list):
									raise KeyError(f"Attempted to access key '{part}' in a list at path {field}")
								else:
									raise KeyError(f"Key {part} not found in response or value is not a dictionary.")
						if isinstance(value, (int, float)):
							raw_metric_key = f"{path}/{field}"
							metric_key = validize_name(raw_metric_key)
							if DEBUG: print(f"Resolved metric_key: {metric_key}")
							if metric_key in METRICS:
								METRICS[metric_key].labels(source=label).set(value)
								if DEBUG: print(f"Set metric {metric_key} to {value}")
							else:
								print(f"Metric key {metric_key} not found in METRICS.")
						else:
							if DEBUG: print(f"Field {field} is not numeric or missing in response for path {path}. Value: {value}")
					except (KeyError, IndexError, TypeError) as e:
						print(f"Error navigating field {field} in response for path {path}: {e}")
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
