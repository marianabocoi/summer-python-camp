"""
Write a program which uses a while loop to sum the squares of integers (starting from 1) until the total exceeds 200.
Print the final total and the last number to be squared and added.
"""
count = 0
the_sum = 0
while the_sum < 200:
    count += 1
    the_sum += count ** 2
print("The sum: ", the_sum, "Last number", count)
