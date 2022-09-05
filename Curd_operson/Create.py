import json
data={"name":"Rajiv","website":"banglore"}
file= open("create.json","w")
json.dump(data,file)
file.close()

