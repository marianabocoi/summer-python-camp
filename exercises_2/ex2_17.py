"""
Find potential sources of logical errors:

product = 0
for i in range(10):
    product *= i

sum_squares = 0
for i in range(10):
    i_sq = i**2
sum_squares += i_sq

nums = 0
for num in range(10):
    num += num
"""
# product should start at 1
# 0 * i will always become 0 resulting in infinte loop
product = 1
for i in range(1,10):
    product *= i
print(product)

# sum_squares should be in the for loop
sum_squares = 0
for i in range(10):
    i_sq = i ** 2
    sum_squares += i_sq
print(sum_squares)

# we want to store the sum in nums not in num
nums = 0
for num in range(10):
    nums += num
print(nums)
