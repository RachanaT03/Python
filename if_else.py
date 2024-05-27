# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 18:09:46 2022

@author: drrac
"""

temperature = input("temperature: ")
temperature = int(temperature)
if temperature < 20:
    print('it is cold')
elif temperature > 20 and temperature < 40:
    print('mild')
else :
    print('hot')
    
          