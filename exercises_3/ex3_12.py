"""
Using loop print the following:
“This person’s name is <name>”
“This person is <age> years old”
“This person is <personality>”
"""

me = {"name": "Molly", "age": 28, "personality": "enfp"}
person = {"name": "Jill", "age": 25, "personality": "intp"}

print(me)
print(person)

my_list = [me, person]
print(my_list)

for person in my_list:
    print("This person’s name is", person["name"])
    print("This person is", person["age"], "years old")
    print("This person is", person["personality"])
    print()
