import json

# Sample JSON string
data = '{"name": "Alice", "age": 30}'

# Decoding the JSON string into a Python object
result = json.loads(data, encoding='utf-8', parse_float=float)

# Returning the decoded object
return result
