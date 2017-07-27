import json

with open('data/person.json') as data_file:
    person = json.load(data_file)

#this is a complex dictionary or list now
print(person)

print(person["age"])
print(person["name"])
print(person["cats"][0])
