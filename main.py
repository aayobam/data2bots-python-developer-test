import json
import os

def read_write_json_data(input_path, output_path):
    # Reads the json file from the file path
    with open(input_path) as f:
        data = json.load(f)

    # Parses the JSON data and extract the "message" key from the json data
    message = data.get("message", {})

    # Extracts the schema information from the "message" key
    schema = {}
    for key, value in message.items():
        data_type = type(value).__name__ # gets the string name for datatypes.
        if data_type == "str":
            schema[key] = {"type": data_type}
        elif data_type == "int":
            schema[key] = {"type": data_type}
        elif data_type == "list":
            if all(isinstance(item, str) for item in value):
                schema[key] = {"type": "string", "enum": value}
            elif all(isinstance(item, dict) for item in value):
                schema[key] = {"type": "array", "items": {}}

    # Step 4: Create the JSON schema output by mapping the data types and adding padding.
    output_schema = {"properties": schema}
    for key, value in output_schema["properties"].items():
        value["tag"] = ""
        value["description"] = ""
        value["required"] = False

    # Step 5: Write the output to the schema directory
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output_path = os.path.join(output_path)
    with open(output_path, "w") as f:
        data = json.dump(output_schema, f, indent=2)
read_write_json_data("./data/data_1.json", "./schema/schema_1.json")
read_write_json_data("./data/data_2.json", "./schema/schema_2.json")
