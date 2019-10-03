#!/usr/bin/python3

import pprint

monthNum = {
    "January": 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June": 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 1
}

capital = {
    "Philippines" : "Manila",
    "Japan" : "Tokyo",
    "South Korea" : "Seoul",
    "Taiwan" : "Taipei"
}

for k, v in monthNum.items():
    print(k, v)

del capital['Japan']

print(capital)