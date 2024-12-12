import requests

def get_request(ip, port, api, https=False, params=None, headers=None, timeout=10):
	"""
	Perform an HTTP GET request.
	"""
	try:
		protocol = "https" if https else "http"
		url = f"{protocol}://{ip}:{port}/{api}"
		response = requests.get(url, params=params, headers=headers, timeout=timeout)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		print(f"GET request failed: {e}")
		return None
	
def parse_restfull(metric, response, source):
	"""
	Parse the RESTful API response.
	"""
	if response:
		try:
			for key, value in response.items():
				if isinstance(value, bool):
					metric.labels(source=source).set(1 if value else 0)
				elif isinstance(value, (int, float)):
					metric.labels(source=source).set(value)
				else:
					print(f"Unsupported type for {key}: {type(value)} - Value: {value}")
		except Exception as e:
			print(f"Failed to parse response for {source}: {e}")
			metric.labels(source=source).set(-1)
	else:
		metric.labels(source=source).set(-1)
		
def json_get(url, property_name, request_id=1):
	"""
	Perform a JSON-RPC GET request.
	
	:param url: The target URL of the JSON-RPC server.
	:param property_name: The property to retrieve.
	:param request_id: The ID for the JSON-RPC request.
	:return: The server's response as a Python dictionary.
	"""
	# Create the JSON-RPC payload
	payload = {
		"jsonrpc": "2.0",
		"method": "property.get",
		"params": {
			"property": property_name
		},
		"id": request_id
	}

	try:
		# Perform the POST request with JSON payload
		response = requests.post(url, json=payload)
		response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
		return response.json()  # Return the JSON response as a dictionary
	except requests.exceptions.RequestException as e:
		print(f"JSON-RPC GET request failed: {e}")
		return None    
    
def validize_name(name):
	return name.replace("/","_").replace("-","_")