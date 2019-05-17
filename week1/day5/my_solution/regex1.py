#floating point number
import re
number=input("enter a string")
if re.fullmatch(r'[+-]*[0-9]*.[0-9]*',number):
    print("True")
else:
    print("False")
