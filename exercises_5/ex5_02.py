"""
Write a Python program to read first n lines of a file.
"""

with open('text.txt', "r") as f:
    first_line = f.readline()

print(first_line)
