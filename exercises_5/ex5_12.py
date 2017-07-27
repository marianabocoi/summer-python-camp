"""
Rewrite the program from exercise 11 so that the exception which is caught in the except clause is re-raised after the error message is printed.
"""


def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
        raise KeyError
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