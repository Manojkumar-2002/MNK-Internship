import json
json_data = '{"name": "John", "age": 30, "city": "New York"}'
python_obj = json.loads(json_data)
print(python_obj)

new_json_data = json.dumps(python_obj)
print(new_json_data)
