"""
Find the syntax errors in the code below and explain why they are errors.
"""

"""
myfunction(x, y):
    return x + y
"""


# needs def before
def myfunction(x, y):
    return x + y


"""
else:
    print("Hello!")
"""
# needs if before!!!
if False:
    pass
else:
    print("Hello!")

"""
if mark >= 50
    print("You passed!")
"""
# missing :
mark = 50
if mark >= 50:
    print("You passed!")

"""
if arriving:
    print("Hi!")
esle:
    print("Bye!")
"""
arriving = False
# typo in else
if arriving:
    print("Hi!")
else:
    print("Bye!")

"""
if flag:
print("Flag is set!")
"""
# missing a tab before print
flag = True
if flag:
    print("Flag is set!")
