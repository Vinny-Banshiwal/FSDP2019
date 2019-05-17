#to find leap year
yr=int(input("Enter a year"))
def leapyr(yr):
    if(yr % 4 == 0):
        return True
    else:
        return False
    
leapyr(yr)