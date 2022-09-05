# import json
# with open("demo.json","r")as json_file:
#     b=json.load(json_file)
#     print(b)

import json
a={"name":"devika","age":"88"}
file= open("salu.json","w")
json.dump(a,file)
file.close()


