# Import necessary modules
from prometheus_client import start_http_server, Gauge
import time

# Define the port for the Prometheus server
PORT = 8002

# Dictionary to hold gauges
gauges = {}

# Function to parse data and create/update gauges
def parse_and_update_gauges(data):
	for i, value in enumerate(data):
		# Handle numeric values
		if isinstance(value, (int, float)):
			# Create gauge programmatically if it doesn't exist
			if i not in gauges:
				gauges[i] = Gauge(f"data_value_{i}", f"Value at index {i} in data array")
			# Update gauge with current value
			gauges[i].set(value)
		# Handle string values
		elif isinstance(value, str):
			# Create a labeled gauge if it doesn't exist
			if i not in gauges:
				gauges[i] = Gauge(f"data_value_{i}", f"String value at index {i} in data array", ['label'])
			# Update the gauge label
			gauges[i].labels(label=value).set(1)  # Set value to 1 for presence

if __name__ == "__main__":
	start_http_server(PORT)
	data = [10, 1.0, "HELLO WORLD"]  # Example data

	while True:
		parse_and_update_gauges(data)
		time.sleep(1)  # Update every second
