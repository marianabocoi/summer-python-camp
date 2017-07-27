"""
Write now the program which you wrote the pseudocode for on the previous exercise.
"""

secret_word = "Bird"
guesses = 10
the_guess = input("What is the word? : ")

while guesses != 1 or the_guess == secret_word:
    the_guess = input("Try again : ")
    guesses -= 1

if the_guess == secret_word:
    print("Congratulations!!!")
else:
    print("You did not guess in time.")