user_input=input("Enter numbers").split()
positive=[]
if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")









