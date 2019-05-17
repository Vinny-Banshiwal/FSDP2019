import math
name=input("Enter name")
ind_spc=name.find(" ")
print(ind_spc)
print(name[ind_spc+1:]+" "+name[0:ind_spc])
