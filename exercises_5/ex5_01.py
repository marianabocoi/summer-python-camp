"""
Write a Python program to read an entire text file.
"""

with open('text.txt', "r") as f:
    read_data = f.read()

print(read_data)
