#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:06:22 2023

@author: carlos
"""

celsius = input("what is the temp in celsius? ")

celsius_float = float(celsius)
# float works best for decimals
fahrenheit = float((celsius_float * 1.8) + 32 ) 

print(fahrenheit)

#I googled to get the formula of 1.8 + 32