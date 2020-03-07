# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:32:58 2020

@author: CEC
"""
"""
def readint(prompt, min, max):
    while True:
        try:
            x=int(input(prompt))
            assert x>= min and x <=max
            return x
            break
        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("El valor debe estar dentro del RANGO --> (-10...10) <---")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
"""
def readint(prompt, min, max):
    while True:
        try:
            x=int(input(prompt))
            assert x>= min and x <=max
            return x
            break
        except ValueError:
            print("Ingresar solo numeros")
        else:
            print("El valor debe estar dentro del RANGO --> (-10...10) <---")
        finally:
            print("Esto es todo!")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
