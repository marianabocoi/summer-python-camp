"""
Write a Python program to read a file line by line and store it into a list.
"""

with open('text.txt', "r") as f:
    lines_list = f.readlines()
print(lines_list)
