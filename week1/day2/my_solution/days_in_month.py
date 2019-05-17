month=int(input("Enter month"))
year= int(input("Enter year"))

def days_in_months(month,year):
    if(year%4==0 and month==2):
        print("28 no of days")
    elif(not year%4==0 and month==2):
        print("29 no of days")
        
        
    elif(month%2==0):
            print("30 no of days")
    elif(not month%2==0):
            print("31 no of days")
            
    else:
        print("28 no of days")
        
print(days_in_months(month,year))