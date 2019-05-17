list1=[5,2,6,2,3]

def addition(list1):
    add=0
    for element in list1:
        add=add+element
    return add
print("addition",addition(list1))


def multiply(list1):
    result=1
    for element in list1:
        result=result*element
    return result
print("multiply",multiply(list1))

def largest(list1):
    for element in list1:
        largest=max(list1)
    return largest
print("largest",largest(list1))

def smallest(list1):
    smallest = min(list1)
    return smallest
print("smallest",smallest(list1))    
        

def sorting(list1):
    sorted_list=sorted(list1)
    return sorted_list
print("sorted",sorting(list1))
    
def duplicate(list1):
    non_dupli=[]
    
    for element in list1:
        
        if element not in non_dupli:
            non_dupli.append(element)
    return non_dupli
print("non duplicate",duplicate(list1))
       


