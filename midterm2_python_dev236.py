# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:13:22 2018

@author: aasup
"""

def fishstore(fish_entry, price_entry):
    dailyspecial = ("Fish Type: " + fish_entry + " " + "costs $" + price_entry)
    return dailyspecial

fish_entry = input("Enter fish name: ")
price_entry = input("Enter fish cost: ")
 
print(fishstore(fish_entry, price_entry))





#fishstore(fish_entry, price_entry)




 
   
