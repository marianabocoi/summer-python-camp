"""
Add a try-except statement to the body of this function which handles a possible IndexError, which could occur if the index provided exceeds the length of the list. Print an error message if this happens:
def print_list_element(thelist, index):
    print(thelist[index])

"""

with open('text.txt', "r") as f:
    text_before = f.read()
print("\nBefore: \n" + text_before)

with open('text_no_new_lines.txt', "w") as f:
    new_text = text_before.replace("\n", "")
    f.write(new_text)

with open('text_no_new_lines.txt', "r") as f:
    text_after = f.read()
print("\nAfter: \n" + text_after)
