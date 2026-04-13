import json


file_path = "sequential.json"

with open(file_path, "r") as file:
    data = json.load(file)

    print  (data)