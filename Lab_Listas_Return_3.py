# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:20:01 2020

@author: carlosortegapolis101
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

def dayOfYear(year, month, day):
    if day < 1 or day >31:
        return none
    else:
        days=0;
        for i in range(1,month):
            days=days+daysInMonth(year,i)
        return days+day

print(dayOfYear(2000, 3, 2))
print(dayOfYear(2000, 12, 31))
print(dayOfYear(2000, 2, 2))
print(dayOfYear(2001, 3, 2))