"""
4. Given the sweden country data convert it into a list with
dictionaries in this form:[ { 'population': 9903122, 'year': 2016}, .... ].
Make a function out of that.
"""
import json

with open('data/sweden.json') as data_file:
    data = json.load(data_file)

my_list = []
for bob in data:
    hello = {"year": bob["date"], "population": bob["value"]}
    print(hello)
    my_list.append(hello)

print(my_list)