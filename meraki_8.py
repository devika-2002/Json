# Q8.Tumhare pass four employes ki details hai list mai:-
import json
a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
dict={}
dict1={}
dict2={}
dict3={}
dict4={}
i=0
while i<len(a):
    dict1[d[i]]=a[i]
    dict2[d[i]]=b[i]
    dict3[d[i]]=c[i]
    dict4[d[i]]=d[i]
    i=i+1
dict["emp1"]=dict1
dict["emp2"]=dict2
dict["emp3"]=dict3
dict["emp4"]=dict4
with open("meraki_8.json","w")as f:
    y=json.dump(dict,f,indent=4)
f.close()

    