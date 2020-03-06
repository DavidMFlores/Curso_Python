# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:19:45 2020

@author: CEC
"""

import pandas as pd
titulos = pd.read_csv('data/titles.csv' )
print(titulos.head(100))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')
print(elenco.head(10))
# Cuantas peliculas estan listadas en el datframe de titulos
print(len(titulos))
# Cual fue la primer pelicula hecha titulada "Romeo and Juliet"?
print(titulos[titulos.title=="Romeo and Juliet"].sort_values('year').head(5))

#

print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))

print(titulos[titulos.title.str.contains("Star Wars")].sort_values('year'))

print(titulos[titulos.title.str.contains("Batman")].sort_values('year'))
a=titulos[titulos.title.str.contains("Taxi Driver")].sort_values('year')
print(titulos[titulos.title.str.contains("Taxi Driver")].sort_values('year'))
print(len(a))

a=titulos[titulos.year==1980]
print(titulos[titulos.year==1980])
print(len(a))


print(titulos[titulos.year.between(1980,2000)])

print(elenco[elenco.n.contains()])


