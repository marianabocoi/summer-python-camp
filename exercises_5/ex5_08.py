"""
Write a Python program to assess if a file is closed or not.
"""
with open('text.txt', "r") as f:
    print(f.closed)
print(f.closed)