import json
import re

def parse_api_file(file_path):
	endpoints = []
	entry = {}

	with open(file_path, 'r') as file:
		lines = file.readlines()

		for line in lines:
			line = line.strip()
			if not line:
				continue

			if re.match(r"^[A-Z ]+$", line):
				if entry and "path" in entry:  # Ensure 'path' key exists before appending
					endpoints.append(entry)
				entry = {"name": line}
			elif line.startswith("Path:"):
				path = line.split("Path:")[1].strip()
				entry["path"] = f"api/{path}"  # Add 'api/' to the beginning of the path
			elif line.startswith("Description:"):
				entry["description"] = line.split("Description:")[1].strip()
			elif line.startswith("Data type:"):
				entry["type"] = line.split("Data type:")[1].strip()
				if entry["type"] == "testpatterntype":
					entry["type"] = "enum"
			elif line.startswith("Range:"):
				entry["range"] = line.split("Range:")[1].strip()
			elif line.startswith("Supported values:"):
				values = line.split("Supported values:")[1].strip()
				entry["supported_values"] = [v.strip() for v in values.split(",")]

		if entry and "path" in entry:  # Append the last entry if it's valid
			endpoints.append(entry)

	return endpoints

if __name__ == "__main__":
	file_path = "API.txt"
	endpoints = parse_api_file(file_path)
	with open("api.py", 'w') as outfile:
		outfile.write(f"endpoints = {json.dumps(endpoints, indent=4)}\n")
	print("Data written to endpoints.py")