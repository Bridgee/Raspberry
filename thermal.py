#!/usr/bin/python3
# -*- coding: utf-8 -*-  
 
file = open("/sys/class/thermal/thermal_zone0/temp")  
temp = float(file.read()) / 1000   
file.close()  
print("CPU Temperature: %.2f °C" %temp)
