#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:06:18 2023

@author: carlos
"""

miles_driven = input("how many miles did your drive? ")

gallons_used = input("how many gallons did you use? ")

#miles_driven_int= int(miles_driven)
#gallons_used_int= int(gallons_used)

miles_driven_float= float(miles_driven)
gallons_used_float= float(gallons_used)

miles_per_gallon = miles_driven_float * gallons_used_float

print(f"Great job you are getting {miles_per_gallon} miles per gallon")

# I was using integer at first then when I switched to float it was giving me the the right answers


