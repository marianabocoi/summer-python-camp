"""
Write a function that takes a list of animals and returns a dictionary where key is an int and the value is an animal.
Input: ["cow", "dog", "cat"]
Output: {1: "cow", 2: "dog", 3: "cat"}

HINT Use for loop

"""


def to_a_map(my_list):
    the_dictionary = {}
    for i in range(len(my_list)):
        the_dictionary[i] = my_list[i]
    return the_dictionary


animal_list = ["cow", "dog", "cat"]
animal_dictionary = to_a_map(animal_list)

print(animal_list)
print(animal_dictionary)
