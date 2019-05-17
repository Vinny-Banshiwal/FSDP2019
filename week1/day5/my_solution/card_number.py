
import re

card_list=[]

while(True):
    
    
    card_no=input("card number")
#    card_number=card_no.split()
    if not card_no:
        break
    else:
        card_list.append(card_no)
    
for item in card_list:
    if re.match(r'[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',item):
        print("True")
    else:
        print("false")