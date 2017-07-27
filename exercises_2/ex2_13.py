"""
Write a program which repeatedly prompts the user for an integer.
If the integer is even, print the integer.
If the integer is odd, don’t print anything.
Exit the program if the user enters the integer 99.
"""
number = 0
while number != 99:
    number = int(input("Give me a number: "))
    if number % 2 == 0:
        print(number)
