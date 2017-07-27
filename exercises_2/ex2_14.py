"""
Implement a simple calculator with a menu.
Display the following options to the user, prompt for a selection, and carry out the requested action
(e.g. prompt for two numbers and add them).
After each operation, return the user to the menu.
Exit the program when the user selects 0.
If the user enters a number which is not in the menu, ignore the input and redisplay the menu.
You can assume that the user will enter a valid integer.

-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers
"""
option = ""
while option != "0":
    option = input(
        "-- Calculator Menu --\n 0. Quit\n 1. Add two numbers\n 2. Subtract two numbers\n 3. Multiply two numbers\n 4. Divide two numbers \n Choose an option: ")
    if option == "1":
        print("Will add the following numbers:")
        number1 = int(input("number1 = "))
        number2 = int(input("number2 = "))
        print("The result of number1 + number2 = ", number1 + number2)

    if option == "2":
        print("Will subtract the following numbers:")
        number1 = int(input("number1 = "))
        number2 = int(input("number2 = "))
        print("The result of number1 - number2 = ", number1 - number2)

    if option == "3":
        print("Will multiply the following numbers:")
        number1 = int(input("number1 = "))
        number2 = int(input("number2 = "))
        print("The result of number1 * number2 = ", number1 * number2)

    if option == "4":
        print("Will divide the following numbers:")
        number1 = int(input("number1 = "))
        number2 = int(input("number2 = "))
        print("The result of number1 / number2 = ", number1 / number2)
