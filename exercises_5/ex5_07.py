"""
Write a Python program to write a list to a file.
"""

my_list = ["Elsa", "Alice", "Maja", "Agnes", "Lilly", "Olivia", "Julia", "Ebba", "Linnea", "Molly", "Ella",
           "Wilma", "Klara", "Stella"]

with open('names.txt', "w") as f:
    for name in my_list:
        f.write(name +"\n")