# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:48:12 2020

@author: David Flores

Ejercicio para importar datos de un fichero

"""
import pandas as pd
titulos = pd.read_csv('data/titles.csv')
print(titulos.head(100))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')
print(elenco.head(10))

print(titulos[titulos.year.between(1980,2000)])
