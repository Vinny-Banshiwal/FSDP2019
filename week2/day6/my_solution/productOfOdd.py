#to multiply odd number
s = reduce(lambda x,y:x*y,(filter(lambda x:x%2==1,map(int, input("enter numbers").split(',')))))
print("Multiplication",s)