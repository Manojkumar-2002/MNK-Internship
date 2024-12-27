import json

with open('json_data.json', 'r') as file:
    data = json.load(file)
with open('new_data.json', 'w') as file:
    json.dump(data, file)

