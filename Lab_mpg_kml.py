# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:23:57 2020

@author: David Flores

Laboratorio: conversion de unidades
"""

def l100kmtompg(liters):
    a=liters*1609.344/3.785411784/1000/100
    return 1/a

def mpgtol100km(miles):
    a=miles*1609.344/3.785411784/1000/100
    return 1/a

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))


