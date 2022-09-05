# import json
# file=open("posts.json","r")
# x=file.read()
# finaldata=json.loads(x)
# print(finaldata)

import json
file=open("posts.json","r")
x=file.read()
finaldata=json.loads(x)
for i in finaldata:
    print(i)
    # print(i["a"])

