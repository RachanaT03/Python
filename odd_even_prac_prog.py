# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:33:07 2023

@author: drrac
"""

list_of_num = [1,2,3,4,5,6,7,8,9,10]

odd_list = []
even_list = []
odd_count = 0
even_count = 0

for x in list_of_num:
    if x % 2 == 0:
        even_list.append(x)
        even_count = even_count + 1
    
    else:
        odd_list.append(x)
        odd_count = odd_count + 1
print("Odd numbers: ",odd_list)
print("Even numbers: ",  even_list)



print("odd count: ",odd_count)


print("even count: ",even_count)




    


 