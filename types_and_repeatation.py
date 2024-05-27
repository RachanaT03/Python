# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:16:28 2023

@author: drrac
"""

list1 = [1,2,3]
list2 = [1,8,5,4,3,9]
common_numbers = []
repeatation = 0

for x in list1:
    if x in list2:
        common_numbers.append(x)
        repeatation = repeatation + 1
print("common numbers = ", common_numbers)
print("repeatation: ",repeatation)
