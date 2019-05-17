list1=[0,2,11]
small=list1[0]
big=list1[1]
target=list1[2]
def row_of_brick(small,big,target):
    if((target%5<=small) and (target-(big*5)<=small)):
        return True
    else:
        return False
    
row_of_brick(small,big,target)