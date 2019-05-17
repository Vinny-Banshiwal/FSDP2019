import re
list1=[]
names=[]
with open("simpsons_phone_book.txt","rt") as fp:
    content=fp.readlines()
    for item in content:
        if re.match(r'^J.*[Neu]',item):
            print(item)
#   
#        list1.append(item.split())
#    for name in list1:
#        names.append(" ".join(name[:-1]))
#        
#for item in names:
   
        
