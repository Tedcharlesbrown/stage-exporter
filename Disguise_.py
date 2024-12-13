from prometheus_client import Gauge, REGISTRY
from functions import validize_name, get_request
from API.Disguise.api import endpoints

DEBUG = False

METRICS = {}
METRIC_PREFIX = "disguise_"

# Recursively process the response and add gauges for numeric or boolean fields
def process_response(response, base_path="", description="", label="source"):
	if isinstance(response, dict):
		for key, value in response.items():
			current_path = f"{base_path}/{key}" if base_path else key
			if isinstance(value, (int, float, bool)):
				metric_name = f"{METRIC_PREFIX}{validize_name(current_path)}"
				if DEBUG: print(f"Processing field {current_path} with value {value}")
				if metric_name not in REGISTRY._names_to_collectors:
					METRICS[current_path] = Gauge(
						metric_name,
						description,
						[label]
					)
				METRICS[current_path].labels(source=label).set(value)
			elif isinstance(value, dict):
				process_response(value, current_path, description, label)
			elif isinstance(value, list):
				for index, item in enumerate(value):
					process_response(item, f"{current_path}[{index}]", description, label)

# Collect metrics dynamically from the response
def collect_metrics(target, label):
	ip, port = target.split(":")
	for endpoint in endpoints:
		path = endpoint['path']
		description = endpoint['description']
		try:
			response = get_request(ip, port, path)
			if DEBUG: print(f"Raw Response for {path}: {response}")
			if response is not None:
				process_response(response, base_path=path, description=description, label=label)
			else:
				print(f"Empty response for path {path} from target {target}.")
		except Exception as e:
			print(f"Failed to fetch or set metric for {path}: {e}")

# Sort metrics alphabetically by source label
def sort_metrics():
	for metric_name, metric in METRICS.items():
		if hasattr(metric, '_metrics'):
			metric._metrics = {
				k: v for k, v in sorted(metric._metrics.items(), key=lambda item: item[0][0])
			}
