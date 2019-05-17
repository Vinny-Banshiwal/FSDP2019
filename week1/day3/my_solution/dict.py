string=input("enter string")
list1=[]


for item in string:
    if item not in list1:
        list1.append(item)
        
dic={}

for item in list1:
    counter=0
    for element in string:
        if(item==element):
            counter=counter+1
    dic[item]=counter
print(dic)