#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:06:20 2023

@author: carlos
"""

fahrenheit = input("what is the temp in fahrenheit? ")

fahrenheit_float = float(fahrenheit)

celsius = float((fahrenheit_float - 32) * .5556 ) 

print(celsius)

#I did the same thing as the previus problem, but changed fahrenheit to celsius and the formula to -32 * .5562222