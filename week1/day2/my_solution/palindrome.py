list1=['12','91','61','51','14']
list2=[]
for element in list1:
    if(element==element[::-1]):
        list2.append("true")
    else:
        list2.append("False")
if('true'in list2):
    print("True")
else:
    print("False")


    