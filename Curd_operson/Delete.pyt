import json
a={'a':2,'b':9,'c':5}
file= open("devi.json","w")
b=a.clear()
json.dump(b,file)

file.close()