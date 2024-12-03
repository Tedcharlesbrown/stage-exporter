from functions import validize_name, get_request
from prometheus_client import Gauge, start_http_server
import time

METRICS = {}
METRIC_PREFIX = "disguise_"

endpoints = [
    {"path": "api/session/status/session", "description": "Return the session config", "returns": ["isRunningSolo", "isDirectorDedicated", "Actors", "Understudies"]},
    # {"path": "api/session/status/project", "description": "Return the project information", "returns": ["major", "minor", "hotfix", "revision"]},
]

# Initialize Gauges
for endpoint in endpoints:
    path = endpoint["path"]
    for key in endpoint["returns"]:
        metric_name = f"{METRIC_PREFIX}{validize_name(path)}_{validize_name(key)}"
        METRICS[metric_name] = Gauge(metric_name, key, ["source"])


def collect_metrics():
    for endpoint in endpoints:
        path = endpoint["path"]
        
        # Get the response from the API
        try:
            response = get_request("127.0.0.1", "80", path)
            result = response.get("result", {})
        except Exception as e:
            print(f"Failed to fetch or parse response for {path}: {e}")
            result = {}
        
        for key in endpoint["returns"]:
            metric_name = f"{METRIC_PREFIX}{validize_name(path)}_{validize_name(key)}"
            
            try:
                value = result.get(key, -1)
                METRICS[metric_name].labels(source="source").set(value)
            except Exception as e:
                print(f"Failed to set metric {metric_name} for key {key}: {e}")


if __name__ == "__main__":
    # Start the HTTP server
    start_http_server(8002)
    print("Prometheus metrics server started on port 8002.")
    
    # Periodically collect metrics
    while True:
        collect_metrics()
        time.sleep(5)
