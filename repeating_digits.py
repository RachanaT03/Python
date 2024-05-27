# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:48:01 2023

@author: drrac
"""

my_list = [1,2,3,4,1,3,7,4,2,1,4,5]   

repeating_digits = {}

for x in my_list:
    if x in repeating_digits:
        repeating_digits[x] = repeating_digits[x] + 1
      
    else:
        repeating_digits[x] = 1
print(repeating_digits)
            
        
    
        
        