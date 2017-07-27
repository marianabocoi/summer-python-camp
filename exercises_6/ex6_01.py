"""
1. Find the year with lowest population in Sweden.
Hint use loops and min.
"""

import json

with open('data/sweden.json') as data_file:
    data = json.load(data_file)
# print(data)

low_value = data[0]["value"]
low_year = data[0]["value"]

for blob in data:
    value = int(blob["value"])
    if value < low_value:
        low_value = value

print(low_value)

for blob in data:
    year = int(blob["date"])
    if int(blob["value"]) == low_value:
        low_year = year

print(low_year)

"""
for blob in data:
    if int(blob["value"]) == low_value:
        print(blob["date"])

"""
