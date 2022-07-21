# Q.2 Python object ko json data main convert karne ka program likho?
{
    "name": "David", 
    "class": "I", 
    "age": 6
}
import json
dict= {"name": "David", "class": "I", "age": 6}
file=open("devika.json","w")
json.dump(dict,file,indent=3)
file.close
