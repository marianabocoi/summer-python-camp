"""
Write a function that takes an int and returns different messages saying in what range the int is in.
For example: the function takes 5 and returns "Your int is in range 0-10", or if the function takes 11 it could return "Your int is in range 11-20".
Return at least 3 different messages.

HINT
What happens if you, in the python interpreter, write the following code:
	if 1 in range(0, 2):
    print("1 is in range 0-2")
 What happens if you change 1 to 3?

HINT
Use if, else, elif statements.
"""

def what_range(number):
    if number in range(0,10):
        return str(number)+" is in range 0-10."
    elif number in range(10,20):
        return str(number)+" is in range 10-20."
    elif number in range(20,30):
        return str(number)+" is in range 20-30."
    elif number <0:
        return str(number) + " is in range -inf-0."
    else:
        return str(number)+" is in range 30-inf."

print(what_range(-1))
print(what_range(0))
print(what_range(3))
print(what_range(10))
print(what_range(20))
print(what_range(30))
print(what_range(50))