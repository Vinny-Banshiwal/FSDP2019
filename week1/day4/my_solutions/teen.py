dict1={'a':2,'b':15,'c':13}

sum1=0

def fix_item(n):
    for item in dict1:
        if n in [13,14,17,18,19]:
            return 0
        else:
            return n
#recurrsive call 
def summ(a,b,c):
    return fix_item(a)+fix_item(b)+fix_item(c)


print(summ(2,15,13))