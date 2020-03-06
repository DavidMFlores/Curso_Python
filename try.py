# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:44:27 2020

@author: CEC
"""

"""
try:
    print("1")
    x=1/0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")
"""

try:
    x=int(input(" Ingrese un numero: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir para cero. sorry.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Algo malio sal...")
print("Se acabo.")