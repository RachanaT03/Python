# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:14:14 2023

@author: drrac
"""

num1 = input("Number 1: ")
num2 = input("Number 2: ")
num1 = int(num1)
num2 = int(num2)

arithmetic_operation = input("Arithemetic operation: ")

if arithmetic_operation == "add":
    result = num1 + num2
    print(result)

elif arithmetic_operation == "subtract":
    result = num1 - num2
    print(result)
    
elif arithmetic_operation == "multiply":
    result = num1 * num2
    print(result)
    
else:
    result = num1 / num2
    print(result)

