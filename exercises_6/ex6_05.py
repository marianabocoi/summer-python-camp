"""
5. Create a list where you have the year pairs and the growth from one year to another.
Example [ { 'pair': '2015-2016', 'growth': 103936}, .... ].
"""

import json


def cucumber(pickles):
    puppies = []
    for i in range(1, len(pickles)):
        pop_grow = int(pickles[i - 1]["value"]) - int(pickles[i]["value"])
        years = pickles[i]["date"] + "-" + pickles[i - 1]["date"]
        print(years, pop_grow)
        puppies.append({'pair': years, 'growth': pop_grow})
    return puppies


with open('data/sweden.json') as data_file:
    data = json.load(data_file)

unicorn = cucumber(data)
print(unicorn)
