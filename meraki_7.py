# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
# Json_file.json:-
# {"Name": "Abhishek","Designation": "CEO of navgurukul","Gender":"male","Age": "29"}

import json
# from msvcrt import kbhit
a={}
filename="meraki7.file"
with open("devika")as f:
    for i in f:
        key,value=i.strip().split(None,1)
        a[key]=value
print(json.dumps(a,indent=4))
file=open("meraki_7.json","w")
json.dump(a,file,indent=4)
file.close()