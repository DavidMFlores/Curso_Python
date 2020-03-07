# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:50:47 2020

@author: CEC
"""
devices=[]
mi_archivo=open("devices.txt","r")

for item in mi_archivo:
    item=item.strip()
    devices.append(item)
    
mi_archivo.close()