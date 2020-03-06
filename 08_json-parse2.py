# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:52:47 2020

@author: CEC
"""

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A succesfull route call.\n")