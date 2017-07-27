"""
This function adds an element to a list inside a dict of lists.
Rewrite it to use a try-except statement which handles a possible KeyError
if the list with the name provided doesn’t exist in the dictionary yet, instead of checking beforehand whether it does.
def add_to_list_in_dict(thedict, listname, element):
    if listname in thedict:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    else:
        thedict[listname] = []
        print("Created %s." % listname)

    thedict[listname].append(element)

    print("Added %s to %s." % (element, listname))
HINT There are two other clauses that we can add to a try-except block: else and finally.
else will be executed only if the try clause doesn’t raise an exception

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Please, write a number!")
else:
    print("I see that you are %d years old." % age)
finally:
    print("Bye!")
"""

def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    thedict[listname].append(element)
    return thedict


my_dict = {}
my_dict = add_to_list_in_dict(my_dict, "names", "Lucy")
my_dict = add_to_list_in_dict(my_dict, "names", "Ada")
my_dict = add_to_list_in_dict(my_dict, "names", "Mei")
my_dict = add_to_list_in_dict(my_dict, "fruits", "pinapple")
my_dict = add_to_list_in_dict(my_dict, "fruits", "apple")
my_dict = add_to_list_in_dict(my_dict, "fruits", "orange")

print(my_dict)