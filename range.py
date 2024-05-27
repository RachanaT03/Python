# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:13:46 2023

@author: drrac
"""

#range

my_list = range(5)
print(my_list)

for items in my_list:
    print(items)

for x in range(5):
    print('hi')
    
#to take 5 input from the user

for x in range(5):
    num = input("Number:")
    print(int(num)*10)
