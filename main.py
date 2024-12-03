import time
import os, yaml
from prometheus_client import start_http_server
from Brompton_Tessera import METRICS as BROMPTON_METRICS
from Disguise import METRICS as DISGUISE_METRICS

from functions import get_request, parse_restfull, json_get

SCRAPE_INTERVAL = 15

# Function to load configuration from .yaml or .yml
def load_config(config_path="config.yaml"):
    """
    Load configuration from a YAML or YML file.
    """
    if not os.path.exists(config_path):  # If default config.yaml is missing
        alt_path = config_path.replace(".yaml", ".yml")
        if os.path.exists(alt_path):
            config_path = alt_path
        else:
            raise FileNotFoundError(f"Neither {config_path} nor {alt_path} exists.")
    with open(config_path, "r") as config_file:
        return yaml.safe_load(config_file)




        
def get_global_settings(config):
    """
    Extract global settings from the YAML configuration.
    """
    global SCRAPE_INTERVAL
    SCRAPE_INTERVAL = int(config.get("global", {}).get("scrape_interval", "15s").rstrip("s"))


def collect_metrics():
    """
    Collect metrics by querying the API and updating Prometheus gauges.
    """
    while True:
        for scrape_config in config["scrape_configs"]:
            for static_config in scrape_config["static_configs"]:
                device = static_config["device"]  # Extract device type (optional for further logic)
                targets = static_config["targets"]  # List of targets
                label = static_config["label"]  # Use the label for the "source" field

                for target in targets:
                    ip, port = target.split(":")  # Split "ip:port" into components

                    # for path, metric in BROMPTON_METRICS.items():
                    for path, metric in DISGUISE_METRICS.items():
                        response = get_request(ip, port, path)
                        parse_restfull(metric, response, label)

        time.sleep(SCRAPE_INTERVAL)  # Use the global SCRAPE_INTERVAL
        

if __name__ == "__main__":
    config = load_config()
    get_global_settings(config)
    start_http_server(8002)  # Expose metrics at localhost:8000
    collect_metrics()
