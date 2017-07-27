"""
Write a Python program to append text to a file and display the text.
"""
with open('text.txt', "r") as f:
    text_before = f.read()
print("\nBefore: \n" + text_before)

with open('text.txt', "a") as f:
    f.write("\nI add this line to thee")

with open('text.txt', "r") as f:
    text_after = f.read()
print("\nAfter: \n" + text_after)
