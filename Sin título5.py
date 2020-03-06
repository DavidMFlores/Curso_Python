# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:59:28 2020

@author: CEC
"""

def wishes():
    return "Happy Birthday!"

w=wishes()
print(w)     # Outputs: Happy Birthday!


def wishes():
    print("My wishes")
    return "Happy Birthday!"

wishes()     # Outputs: My wishes


def wishes():
    print("My wishes")
    return "Happy Birthday!"

print(wishes())     # Outputs:  My wishes
                    #           Happy Birthday