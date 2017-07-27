"""
Write a Python program to read a file line by line store it into a variable.
"""
content = {}
with open('text.txt', "r") as f:
    count = 0
    for line in f:
        content [count] = line
        count += 1
print(content)
