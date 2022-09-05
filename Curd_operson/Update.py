import json
a={'a':2,'b':9,'c':5}
file= open("devi.json","w")
a.update({'a':10})
json.dump(a,file)
file.close()

