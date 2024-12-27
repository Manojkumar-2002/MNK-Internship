import json
python_dict = {"name": "John", "age": 30, "city": "New York"}
json_data = json.dumps(python_dict, sort_keys=True, indent=4)
print(json_data)
