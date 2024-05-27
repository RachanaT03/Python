# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 19:44:49 2022

@author: drrac
"""

#difference b/w lists and sets
#1. list can have duplicate items but a set has unique items.
#2. items are stored in a sequence in a list but randomly in a set.

# syntax related to sets: 
#1. how to create a set

my_set = {5,6,7,8,9,123,456,6,6}
print(my_set)

#add elements to set
my_set.add(67)
print(my_set)

#removing element from the set
my_set.discard(67)
print(my_set)

#union of two sets
#syntax= set1.union(set2)
set1 = {4,5,6,7,8,9,10,34}
set2 = {1,2,3,11,12,13,34}
union_set = set1.union(set2)
print(union_set)

#intersection of two sets
#syntax = set1.intersection(set2)

inter_set = set1.intersection(set2)
print(inter_set)