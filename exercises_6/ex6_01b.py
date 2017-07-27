"""
1. Find the year with lowest population in Sweden.
Hint use loops and min.
"""

import json

with open('data/sweden.json') as data_file:
    data = json.load(data_file)
# print(data)

minimmum = int(data[0]["value"])
min_year = data[0]["date"]

for i in range(1, len(data)):
    current_value = int(data[i]["value"])
    if minimmum > current_value:
        minimmum = current_value
        min_year = data[i]["date"]

print(min_year)
