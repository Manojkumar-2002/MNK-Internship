import json
json_data = '{"real": 3, "imag": 4}'
python_obj = json.loads(json_data)
def contains_complex(obj):
    return isinstance(obj, dict) and 'real' in obj and 'imag' in obj
print(contains_complex(python_obj))
