# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:46:51 2020

@author: shri
"""

dict = {"Name":"Saish Wadkar","Age":22,"DOB":"27 April 1998"}

for i in dict.items():
    print(i)

print()    
keys=dict.keys()    
print("Keys --- ",keys,"Type ---",type(keys))
print()
values=dict.values()
print("Values --- ",values,"Type ---",type(values))