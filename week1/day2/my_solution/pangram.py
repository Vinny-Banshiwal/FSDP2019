import string

list1=input("Enter string")
list2=list(list1.lower())
a_z=list(string.ascii_lowercase)
output=[]
for element in list2:
    if(element not in output):
        output.append(element)


       