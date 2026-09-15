import json

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "hiking"]
}

with open("data.json", "w") as f:
    json.dump(data, f)