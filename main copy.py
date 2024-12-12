import time
import os
import yaml
from prometheus_client import start_http_server
from functions import get_request, parse_restfull, json_get

SCRAPE_INTERVAL = 15

# Define modules globally
modules = {
	"brompton-tessera": "Brompton_Tessera",
}

def load_config(config_path="config.yaml"):
	if not os.path.exists(config_path):
		alt_path = config_path.replace(".yaml", ".yml")
		if os.path.exists(alt_path):
			config_path = alt_path
		else:
			raise FileNotFoundError(f"Neither {config_path} nor {alt_path} exists.")
	with open(config_path, "r") as config_file:
		return yaml.safe_load(config_file)

def get_global_settings(config):
	global SCRAPE_INTERVAL
	SCRAPE_INTERVAL = int(config.get("global", {}).get("scrape_interval", "15s").rstrip("s"))

def collect_metrics(config):
	while True:
		for scrape_config in config["scrape_configs"]:
			for static_config in scrape_config["static_configs"]:
				device = static_config["device"]
				targets = static_config["targets"]
				label = static_config["label"]

				module_name = modules.get(device)
				if not module_name:
					print(f"Unsupported device type: {device}")
					continue
				module = __import__(module_name)
				for target in targets:
					module.collect_metrics(target, label)

		time.sleep(SCRAPE_INTERVAL)

if __name__ == "__main__":
	config = load_config()
	get_global_settings(config)
	start_http_server(8002)
	collect_metrics(config)
