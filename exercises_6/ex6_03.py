"""
3. What is the minimum and maximum population growth years.
Make a function out of that. Hint, use inbuilt min, max functions.
"""

import json

def cucumber(pickles):
    puppies = {}
    for i in range(1, len(pickles)):
        pop_grow = int(pickles[i - 1]["value"]) - int(pickles[i]["value"])
        years = pickles[i]["date"] + "-" + pickles[i - 1]["date"]
        print(years, pop_grow)
        puppies[pop_grow] = years
    return puppies

with open('data/sweden.json') as data_file:
    data = json.load(data_file)


unicorn = cucumber(data)
print(unicorn)
min_pop_grow = min(unicorn)
print(min_pop_grow)
print(unicorn[min_pop_grow])

max_pop_grow = max(unicorn)
print(max_pop_grow)
print(unicorn[max_pop_grow])