import json
data={"name":"devika","work":"devloper"}
with open("remo.json","w")as json_file:
    json.dump(data,json_file)