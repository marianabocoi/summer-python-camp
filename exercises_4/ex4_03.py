"""
Use function from exercise 1. and function from exercise 2. to return a circle circumference. Write this code in a third file.
"""
from exercises_4.ex4_01 import diameter
from exercises_4.ex4_02 import circumference

my_circle_radius = 2
my_circle_circumference = circumference(diameter(my_circle_radius))
print(my_circle_circumference)
