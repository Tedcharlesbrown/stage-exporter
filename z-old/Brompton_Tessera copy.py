from prometheus_client import Gauge
from functions import validize_name, get_request

METRICS = {}
METRIC_PREFIX = "tessera_"

model_ports = [
	{"model": "sx40", "sdi-port": 1, "hdmi-port": 1},
]

endpoints = [
	{"path": "api/system/processor-type", "description": "Processor hardware model", "type": "enum", "supported_values": ["m2", "s4", "s8", "t1", "t8", "sx40"]},
	# 3.5.1 API
	# STATISTICS
	# {"path": "api/devices/statistics/associated-count", "description": "The number of devices currently being controlled by the processor", "type": "int", "range": "0 - 2200"},
	# {"path": "api/devices/statistics/error-count", "description": "The number of online devices currently reporting an error state", "type": "int", "range": "0 - 2048"},
	# {"path": "api/devices/statistics/online-count", "description": "The number of online devices currently detected by the processor", "type": "int", "range": "0 - 2048"},
	# {"path": "api/devices/statistics/online-count", "description": "The number of online devices currently detected by the processor", "type": "int", "range": "0 - 2048"},
	# GROUP
	# - not yet inmplemented
	# INPUT
	# {"path": "api/input/active/source/port-number", "description": "Which physical port instance is currently enabled for video input. For example, SDI A = port 1, SDI B = port 2. The available number of port instances for any port type will vary based on the processor hardware variant.", "type": "int", "range": "1 - 2"},
 	# {"path": "api/input/active/source/port-type", "description": "Which physical port instance is currently enabled for video input. The available types will vary based on the processor hardware variant.", "type": "enum", "supported_values": ["dvi", "hdmi", "sdi"]},
	# DVI	
 	{"path": "api/input/ports/dvi/[dvi-port]/controls/colour-space/colour", "description": "Gets or sets the colour space used for the incoming DVI content", "type": "enum", "supported_values": ["rec-2020", "dci-p3", "rec-709", "aces-cg", "custom"]},
 	{"path": "api/input/ports/hdmi/[hdmi-port]/controls/colour-space/colour", "description": "Gets or sets the colour space used for the incoming DVI content", "type": "enum", "supported_values": ["rec-2020", "dci-p3", "rec-709", "aces-cg", "custom"]},
	
	# OLD API
	# {"path": "api/input/active/refresh-rate", "description": "Active video input refresh rate", "type": "float", "range": "23.5 - 241.0"},
	# {"path": "api/input/active/resolution/height", "description": "Active video input height", "type": "int", "range": "32 - 4096"},
	# {"path": "api/input/active/resolution/width", "description": "Active video input width", "type": "int", "range": "32 - 4096"},
	# {"path": "api/output/global-colour/brightness", "description": "Write -1 to reset output brightness to calculated common maximum for available fixtures.", "type": "float", "range": "-1 - 10000"},
	# {"path": "api/output/global-colour/colour-temperature", "description": "Gets or sets the output colour temperature", "type": "float", "range": "2000 - 11000"},
	# {"path": "api/output/global-colour/dark-magic/enabled", "description": "Enables or disables the processor's Dark Magic feature", "type": "bool"},
	# {"path": "api/output/global-colour/gains/blue", "description": "Gets or sets the value of the output blue gain", "type": "float", "range": "0 - 100"},
	# {"path": "api/output/global-colour/gains/green", "description": "Gets or sets the value of the output green gain", "type": "float", "range": "0 - 100"},
	# {"path": "api/output/global-colour/gains/intensity", "description": "Gets or sets the value of the output intensity gain", "type": "float", "range": "0 - 100"},
	# {"path": "api/output/global-colour/gains/red", "description": "Gets or sets the value of the output red gain", "type": "float", "range": "0 - 100"},
	# {"path": "api/output/global-colour/gamma", "description": "Gets or sets the value of the output gamma", "type": "float", "range": "0.2 - 4.0"},
	# {"path": "api/output/global-colour/puretone/enabled", "description": "Enables or disables PureTone", "type": "bool"},
	# {"path": "api/output/network/failover/settings/enabled", "description": "Enables or disables failover mode on the processor", "type": "bool"},
	# {"path": "api/output/network/failover/settings/modes/on-button-press", "description": "Enables or disables failover to backup processor when the processor's Blackout/Freeze buttons are pushed", "type": "bool"},
	# {"path": "api/output/network/failover/settings/modes/on-partner-fail", "description": "Enables or disables partner processor failover when processor failure is detected (e.g. the processor loses power)", "type": "bool"},
	# {"path": "api/output/network/failover/settings/modes/on-partner-video-fail", "description": "Enables or disables partner processor failover on video signal loss", "type": "bool"},
	# {"path": "api/output/network/failover/settings/modes/prefer-primary", "description": "If prefer primary processor failover mode is activated, when primary processor is functioning correctly, it will be automatically always be the active processor", "type": "bool"},
	# {"path": "api/output/network/failover/settings/role", "description": "Is processor's failover role Primary or Backup", "type": "enum", "supported_values": ["primary", "backup"]},
	# {"path": "api/output/network/failover/state/is-active", "description": "Whether failover is active on the processor", "type": "bool"},
	# {"path": "api/output/network/failover/state/is-partner-present", "description": "Whether the backup processor is currently online and detected", "type": "bool"},
	# {"path": "api/override/blackout/enabled", "description": "Enables or disables blackout", "type": "bool"},
	# {"path": "api/override/blackout/fade-time", "description": "The value of the blackout fade time. The fade time may be adjusted between zero (snap) and 10 seconds", "type": "float", "range": "0.0 - 10.0"},
	# {"path": "api/override/freeze/enabled", "description": "Enables or disables video freeze", "type": "bool"},
	# {"path": "api/override/test-pattern/enabled", "description": "Enables or disables test pattern output function", "type": "bool"},
	# {"path": "api/override/test-pattern/format", "description": "Format of the generated test pattern", "type": "enum", "supported_values": ["from-input", "standard-dynamic-range", "perceptual-quantiser", "hybrid-log-gamma"]},
	# {"path": "api/override/test-pattern/type", "description": "Determines which test pattern to generate. Defaults to SMPTE bars", "type": "enum", "supported_values": ["brompton", "brompton-overlay", "red", "green", "blue", "cyan", "magenta", "yellow", "white", "black", "grid", "scrollinggrid", "checkerboard", "scrolling-checkerboard", "colour-bars", "gamma", "gradient", "scrolling-gradient", "strobe", "smpte-bars", "scrolling-smpte-bars", "custom", "forty-five-degree-grid", "scrolling-forty-five-degree-grid"]},
	# {"path": "api/panels/statistics/associated-count", "description": "The number of panels currently being controlled by the processor", "type": "int", "range": "0 - 2200"},
	# {"path": "api/panels/statistics/error-count", "description": "The number of online panels currently reporting an error state", "type": "int", "range": "0 - 2048"},
	# {"path": "api/panels/statistics/online-count", "description": "The number of online panels currently detected by the processor", "type": "int", "range": "0 - 2048"},
	# {"path": "api/processing/colour-correct/enabled", "description": "Enables or disables the processor's 14-Way Colour Correct feature", "type": "bool"},
	# {"path": "api/processing/colour-replace/enabled", "description": "Enables or disables the processor's Colour Replace feature", "type": "bool"},
	# {"path": "api/processing/curves/enabled", "description": "Enables or disables the processor's Colour Curves feature", "type": "bool"},
	# {"path": "api/processing/osca/module-correction-enabled", "description": "Enables or disables OSCA module correction", "type": "bool"},
	# {"path": "api/processing/osca/seam-correction-enabled", "description": "Enables or disables OSCA seam correction", "type": "bool"},
	# {"path": "api/processing/scaler/enabled", "description": "Enables or disables scaler", "type": "bool"},
	# {"path": "api/system/uptime", "description": "Time since processor boot in DDd HHh MMm SSs format", "type": "string"},
	# STRING OUTPUT
	# {"path": "api/output/network/failover/state/partner-absence-duration", "description": "How long the backup processor has been absent for", "type": "string"},
	# {"path": "api/output/network/failover/state/partner-name", "description": "Name of the backup processor", "type": "string"},
	# {"path": "api/output/network/failover/state/partner-serial", "description": "Serial number of the backup processor", "type": "string"},
	# {"path": "api/output/network/failover/state/partner-video-absence-duration", "description": "Time since backup processor video source was last detected", "type": "string"},
	# {"path": "api/presets/active/name", "description": "Name of the currently active preset", "type": "string"},
	# {"path": "api/presets/active/number", "description": "Set to activate a preset", "type": "string"},
	# {"path": "api/system/current-date-time", "description": "Current date/time of processor in yyyy-MM-dd hh:mm:ss 24 hour format", "type": "string"},
	# {"path": "api/system/software-version", "description": "Current version of software in format x.y.z", "type": "string"},
]

def uptime_to_seconds(uptime):
	"""
	Incoming String = '88d 1195h 71608s'
	Takes the Seconds and outputs int
	"""
	for part in uptime.split():
		if part.endswith("s"):
			return int(part[:-1])

# Initialize Prometheus metrics based on the defined endpoints
for endpoint in endpoints:
	description = endpoint['description']
	if 'range' in endpoint:
		description += f" RANGE: {endpoint['range']}"
	if 'supported_values' in endpoint:
		description += f" Supported values: {endpoint['supported_values']}"
	METRICS[endpoint['path']] = Gauge(
		f"{METRIC_PREFIX}{validize_name(endpoint['path'])}",
		description,
		["source"]  # Label for identifying the source
	)

def collect_metrics(target, label):
	ip, port = target.split(":")
	processor_type = get_request(ip, port, endpoints[0]["path"]).get("processor-type", None)

	for endpoint in endpoints:
		path = endpoint["path"]
		# Check if port placeholders exist in the path and replace with the corresponding port number
		if "[" in path:
			for port_type in ["dvi-port", "sdi-port", "hdmi-port"]:
				if port_type in path:
					# Find the model data matching the processor type
					model_data = next((m for m in model_ports if m["model"] == processor_type), None)
					if model_data and port_type in model_data:
						port_number = model_data[port_type]
						path = path.replace(f"[{port_type}]", str(port_number))
						print(path)
					else:
						# Skip the endpoint if the port is not available
						break
			else:
				continue
			# Further processing of the path, e.g., making API calls or metrics collection
			print(f"Processed metric: {path}")
		# if model != "none":
		# 	model_data = next((m for m in model_ports if m["model"] == model), None)
		# 	if model_data:
		# 		for port_type in ["dvi-port", "sdi-port", "hdmi-port"]:
		# 			if port_type in path and port_type not in model_data:
		# 				continue  # Skip paths requiring a port if not present in model data
		# 			if port_type in path:
		# 				path = path.replace(port_type, str(model_data.get(port_type, -1)))
		# 		# Further processing of the path, e.g., making API calls or metrics collection
		# 		print(f"Processed metric: {path}")
		# Fetch data from the device API
		try:
			response = get_request(ip, port, path)
			print("Raw Response:", response)  # Debug: Print the raw API response
			if response is not None:
				# Extract the key from the endpoint's path
				response_key = path.split("/")[-1]
				value = response.get(response_key, None)

				if value is not None:
					if endpoint["type"] == "enum":
						# Handle enums by finding the index of the value in supported_values
						if value in endpoint["supported_values"]:
							index = endpoint["supported_values"].index(value)
							METRICS[path].labels(source=label).set(index)
							# print(f"Set enum metric for {path}: {index}")  # Debug
						else:
							print(f"Unsupported enum value: {value}. Supported values: {endpoint['supported_values']}")
					elif endpoint["path"] == "api/system/uptime":
						# Convert uptime to seconds
						uptime_seconds = uptime_to_seconds(value)
						METRICS[path].labels(source=label).set(uptime_seconds)
						# print(f"Set uptime metric for {path}: {uptime_seconds}")  # Debug
					elif endpoint["type"] == "bool":
						# Handle boolean values (convert to 1 for True and 0 for False)
						boolean_value = 1 if value else 0
						METRICS[path].labels(source=label).set(boolean_value)
						# print(f"Set boolean metric for {path}: {boolean_value}")  # Debug
					elif endpoint["type"] in ["int", "float"]:
						# Handle numerical types
						METRICS[path].labels(source=label).set(value)
						# print(f"Set metric for {path}: {value}")  # Debug
					else:
						print(f"Unsupported type for {path}: {endpoint['type']}")
				else:
					print(f"Response missing expected key '{response_key}' for path {path}.")
			else:
				print(f"Empty response for path {path} from target {target}.")
		except Exception as e:
			print(f"Failed to fetch or set metric for {path}: {e}")
