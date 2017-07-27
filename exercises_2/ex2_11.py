"""
Write the pseudocode for a program which keeps prompting the user to guess a word.
The user is allowed up to ten guesses – write your code in such a way that the secret word
and the number of allowed guesses are easy to change. Print messages to give the user feedback.
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