"""
This is a bigger exercise that will consist of 4 parts. Imagine that you are going on a road trip to Eastern Europe and you want to estimate how long the whole trip will take. You know approximately how many hours it will take you to drive from point a to point b, but you also want to account for staying the night at a hotel/resting.
"""


"""
1. Write a function that takes four parameters departure, destination, duration (in hours), overnight (this parameter should be a boolean). The function should return a dictionary that looks something like this: {'departure': 'sthlm', 'destination': 'oslo', 'duration': 10, 'overnight': True}
"""

"""
2. Write a function that takes a list of travel plans like this: 
['sthlm', 10, True, 'oslo', 11, True, 'copenhagen', 15, False, 'krakow']
The list basically says “I travel from Stockholm. I will drive for 10 hours. I will sleep when I get to Oslo. I travel from Oslo. I will drive for 11 hours… etc...”
Use function a. within function b. (the one you are writing) to return a list like this:
[{'departure': 'sthlm', 'destination': 'oslo', 'duration': 10, 'overnight': True}, {'departure': 'oslo', 'destination': 'copenhagen', 'duration': 11, 'overnight': True}, {'departure': 'copenhagen', 'destination': 'krakow', 'duration': 15, 'overnight': False}]
That is, a list containing dictionaries.
HINT Think about how you will get the information from the input list - how will you use it in the function? Is there some sort of a pattern to the values that are in the list? For example, that every value after the departure value is duration and after duration comes overnight. (The pattern is actually 3 value that are repeating: departure, duration, overnight… How can we get destination?)
HINT You could use range in a for loop to go through the list. Do you remember how to get the length length of a list (that is how many values are in the list)? If you decide to use range, could you use the information that the patterns repeats every 3 values? (Remember  step in range?)
HINT Remember how you can add something to a list?
"""


"""
3. Write a function that takes what function  b. returns and itself returns the sum of hours the whole trip will take. Make sure that if you sleep at some hotel on the way to some destination then 10 hours will be added to the whole trip. 
	So if the input is:
[{'departure': 'sthlm', 'destination': 'oslo', 'duration': 10, 'overnight': True}]
The output should be: 20
And if the input is:
 [{'departure': 'sthlm', 'destination': 'oslo', 'duration': 10, 'overnight': False}]
The output should be: 10

"""

"""
4. Write a function that takes what function b. returns. Inside this function use function c. to return this:
	sthlm -> oslo, will take: 20 hours including sleep ->
oslo -> copenhagen, will take: 21 hours including sleep ->
copenhagen -> krakow, will take: 15 hours ->
The whole trip will take: 56
HINT Remember string concatenation? Remember how you can add a new empty line in a string?
"""