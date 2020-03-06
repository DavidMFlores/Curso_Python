# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:23:28 2020

@author: David FLores

Listas y diccionarios
"""

"""
Listas
"""
hostnames=["R1","R2","R3","S1","S2"]
# En la pantalla de comandos: type(hostnames)
# Out:                        list
# En la pantalla de comandos: len(hostnames)
# Out:                        5
# En la pantalla de comandos: hostnames[0]
# Out:                        'R1'
# En la pantalla de comandos: hostnames[-1]
# Out:                        'S2'
# En la pantalla de comandos: hostnames[0]="RTR1"
# En la pantalla de comandos: hostnames[0]
# Out:                        'RTR!'
# En la pantalla de comandos: del hostnames[2]
# En la pantalla de comandos: hostnames
# Out:                        ['RTR1', 'R2', 'S1', 'S2']

"""
Diccionarios
"""

ipAddress = {"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3"}
# En la pantalla de comandos: type(ipAddress)
# Out:                        dict
# En la pantalla de comandos: ipAddress
# Out:                        {'R1': '10.1.1.1', 'R2': '10.2.2.1', 'R3': '10.3.3'}
# En la pantalla de comandos: ipAddress['R1']
# Out:                        '10.1.1.1'
# En la pantalla de comandos: ipAddress["S1"]="10.1.1.10"  
# En la pantalla de comandos: ipAddress
# Out:                        {'R1': '10.1.1.1', 'R2': '10.2.2.1', 'R3': '10.3.3', 'S1': '10.1.1.10'}
# En la pantalla de comandos: "R3" in ipAddress
# Out:                        True