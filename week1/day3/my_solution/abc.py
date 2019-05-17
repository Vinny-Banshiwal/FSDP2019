string=input("enter a string")
dict1={}
a=0
b=0
for item in string:
    
    
    if( item.isalpha()==True):
        a+=1
    elif(item.isdigit()==True):
        b+=1

    dict1['letter']=a
    dict1['digit']=b
print(dict1)