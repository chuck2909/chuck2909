#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:54:24 2023

@author: carlos
"""
current_time = input("What time is it (in hours)? ")
waiting_time = input("How many hours do you have to wait? ")

current_time_float = float(current_time) # I used float because the time could be for example 1:30, but if yo
waiting_time_float = float(waiting_time)

hours = current_time_float + waiting_time_float

timeofday = hours % 24

print(timeofday)


# I used float because the time could be for example 1:30, but if you do 6.45 + 5.45 you get 11.9. 
#The examples on canvas work, but I can't get the hours added to restart at 0 once it passes 60 min.