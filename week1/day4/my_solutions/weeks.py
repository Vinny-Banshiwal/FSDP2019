days=['Monday','tue','wed','thu','fri','sat','sun']
user_input=list(input("Enter the days").split(","))
print("User input is=",user_input)

for item in days:
    if item not in user_input:
        
        user_input.append(item)
print("output list =",user_input)
        