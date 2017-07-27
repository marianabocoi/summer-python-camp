"""
Which of these fragments are valid and invalid first lines of if statements?
Explain why:

if (x > 4)
if x == 2
if (y =< 4)
if (y = 5)
if (3 <= a)
if (1 - 1)
if ((1 - 1) <= 0)
if (name == "James")
"""
x = 5
if (x > 4):
    print("x greather than 4")

x = 2
if x == 2:
    print("x equal to 2")

y = 4
# <= not =<
# if (y =< 4):
if (y <= 4):
    print("less than or equal to 4")

# == not =
# if (y = 5)
if (y == 5):
    print("y is 5")

a = 3
if (3 <= a):
    print("a is less than or equal to 3")

# 1 - 1 does not evaluate to a boolean
# if (1 - 1):

if ((1 - 1) <= 0):
    print("(1 - 1) <= 0 is True")

name = "James"
if (name == "James"):
    print("it was James")
