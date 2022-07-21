import json
with open("demo.json","r")as json_file:
    b=json.load(json_file)
    print(b)