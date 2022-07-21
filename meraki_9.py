# Apki pass ek shopping name ki ek dictionary hai
import json
a={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
x=input("enter the item:")
c=int(input("enter the number you want:"))
dict={}
dict1={}
a["shopping_list"]["lollipop"]=35
for i in a:
    if x not in a[i]:
        print("item not found")
    else:
        if a[i]==a[i]:
            l=a[i][x]
            s=int(l)
            n=s-c
        for j in a[i]:
            dict[j]=a[i][j]
            if j==x:
                dict[j]=n
                dict1[i]=dict
        print(dict1)
    f=open("merki9_shopping_list.json","w")
    json.dump(dict1,f,indent=4)
    f.close()
