# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:55:08 2020

@author: CEC
"""

def l100kmtompg(liters):
    a=liters*1609.244/3.785411784/100000
    return 1/a

def mpgtol100km(miles):
    a=miles*1609.244/3.785411784/100000
    return 1/a

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
