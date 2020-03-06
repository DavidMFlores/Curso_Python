# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:09:04 2020

@author: David Flores

Funcion para encontrar un numero primo
"""

def esPrimo(n):
    for i in range(2,n):
        if n%i != 0:
            return True
        else:
            return False

"""
num_prueba=[2,3,4,5,6,17,18,13,11]
b=len(num_prueba)
for i in range(b):
    print(esPrimo(num_prueba[i]))
"""

for i in range(1, 20):
	if esPrimo(i + 1):
			print(i + 1, end=" ")
print()
