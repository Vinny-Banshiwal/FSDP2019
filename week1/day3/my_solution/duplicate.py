# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:18:14 2019

@author: Honey
"""

list1=[12,24,35,24,88,120]
list2=[]
for item in list1:
    if item not in list2:
        list2.append(item)
list3=[]
for item in list2:
    output=list2[::-1]
print(output)
        