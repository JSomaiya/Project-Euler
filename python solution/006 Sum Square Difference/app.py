'''
Project Euler Challenge 06: Sum Square Difference

Problem Question:
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ..... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ..... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import math

sum_of_square = 0
square_of_sum = 0

for n in range (1, 101):
    sum_of_square += math.pow(n, 2)
    square_of_sum += n

sum = round(math.pow(square_of_sum, 2) - sum_of_square)

print(sum)