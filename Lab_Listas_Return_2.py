# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:08:13 2020

@author: David Flores

Laboratorio: Listas y Return 2
"""

def isYearLeap(year):
    if (year%4==0) and (year%100!=0 or year%400==0):
        return True
    else:
        return False

def daysInMonth(year, month):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year < 1900 or month < 1 or month > 12:
        return None
    elif isYearLeap(year):
        if month == 2:
            return 29
        else:
            return days[month-1]
    else:
        return days[month-1]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
