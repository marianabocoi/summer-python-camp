"""
2. What is the average population growth between the years.
E.g. between 2015 and 2016 the population growth is 103936.
Hint: To calculate the average of 1 and 2 you would need to run:
numpy.mean([1,2])  output: 1.5. Make a function out of that.

"""
import numpy
import json

with open('data/sweden.json') as data_file:
    data = json.load(data_file)

sofie = []
# current - past
for i in range(1, len(data)):
    print(data[i]["date"])
    print(data[i-1]["date"])
    kittens = int(data[i-1]["value"]) - int(data[i]["value"])
    sofie.append(kittens)
    print(kittens)

print(sofie)
print(int(numpy.mean(sofie)))