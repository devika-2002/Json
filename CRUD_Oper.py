# ishme create hota hai delete v and update v or file ko delete kr deta hai/
# store nhi rhta hai update krte rhta hai/

import json,os
print("WELCOME TO CRUD OPERATION")
print()
print("press 1 for create \n press 2 for read \n press 3 for update \n press 4 for delete ")
print()
def create():
        data=({"name":input("Enter your name: "),
        "email":input("Enter your email: "),"address":input("Enter your address: ")})
        file= open("person.json","w")
        json.dump(data,file)
        file.close()
        print()
        print(" Your info created successfully ")
def read():
    file=open("person.json","r")
    a=json.load(file)
    print(a)
    print()
    print(" Your info read successfully ")

def update():
    a = {"name":input("Enter your name: "),"email":input("Enter your email: "),
                             "address":input("Enter your address: ")}
    
    file= open("person.json","w")
    a.update()
    json.dump(a,file)
    file.close()
    print()
    print(" Your info update successfully ")

def delete():
    os.remove("person.json")
    print(" Your info  delete successfully ")
choice = int(input("Enter your choice: "))
if choice == 1:
    create()
   
elif choice == 2:
    read()
   
elif choice == 3:
    update()
  
elif choice == 4:
    delete()
    
else:
    pass
