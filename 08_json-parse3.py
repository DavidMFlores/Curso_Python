# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:58:33 2020

@author: CEC
"""

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))


"""
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
#orig = "Quito"
#dest = "Guayaquil"
key = "XId47yn59VbYxAdy0YQUAfcqZkKdHxOx"
while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    jsonstatus = jsondata["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
"""
"""
mport urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Tznt11GJzT0W3awGbRvrGPutNBN7Ns0z"
while True:
orig = input("Starting Location: ")
if orig == "quit" or orig == "q":
break
dest = input("Destination: ")
if dest == "quit" or dest == "q":
break
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URL: " + (url))
json_data = requests.get(url).json()
jsonstatus = jsondata["info"]["statuscode"]
if json_status == 0:
print("API Status: " + str(json_status) + " = A successful route call.\n")
"""