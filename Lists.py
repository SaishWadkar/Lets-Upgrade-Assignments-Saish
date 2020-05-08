# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:34:01 2020

@author: shri
"""

myList=[1,2.5,"Hello Everyone",["My name is Saish",5.157,500] ]


myList.insert(0,2500)
myList.remove(2500)
myList.pop(3)
myList.insert(10,6000)
myList.pop()

myList.append(10000)    


itr=0
for i in myList:
    print("Itertion - ",itr,"    Element --- ",i)
    itr+=1
    
    
del myList[2:4]

myList.extend(["Saish",50,60,45.25])
myList.extend([50,50,50,50])

print()


#  Final List
itr=0
for i in myList:
    print("Itertion - ",itr,"  Element --- ",i," Type -",type(i))
    itr+=1
    
myList.reverse()  
print("--- Reverse Order ---")
itr=0
for i in myList:
    print("Itertion - ",itr,"  Element --- ",i," Type -",type(i))
    itr+=1


print()    
print("Index od element '50' ---- ",myList.index(50))
print("Count of element '50' ---- ",myList.count(50))

copyList=myList.copy()
print()
print("--- Copied List --- ")
for i in copyList:
    print(i)


    