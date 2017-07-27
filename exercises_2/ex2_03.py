"""
How can we simplify these code fragments?

if bool(a) == True:
    print("a is true")
if x > 50:
    b += 1
    a = 5
else:
    b -= 1
    a = 5
"""
a = True
if a:
    print("a is true")

x = 30
b = 1
a = 5
if x > 50:
    b += 1

else:
    b -= 1
