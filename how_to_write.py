import pickle
fh=open("write.json","wb")
list=["name","roll","class"]
list1=["sachin","12","5"]
pickle.dump(list,fh)
pickle.dump(list1,fh)
fh.close()
