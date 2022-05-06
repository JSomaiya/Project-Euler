'''
Project Euler Challenge 03. Largest Prime Factor

Problem Question:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor the number 600851475143 ?
'''

# set the number for the question
number = 600851475143

# variable to store the largest prime
max_prime = 0

# variable that holds the maximum number the loop can go to
max_num = number

# loop through all the number from 1
for i in range(1, number + 1): 
    # if the number in i is great than the max number stop loop
    if(i > max_num):
        break
    
    # if the question number modulus (%) i returns 0 
    if number % i == 0:
        # set counter variable to check prime
        count = 0

        # loop through to check prime
        for j in range (1, i + 1):
            # if multiple is found add 1 to cound
            if i % j == 0:
                count += 1

        # only change max prime if 2 multiples are found
        if count == 2:
            max_prime = i
            max_num = number / i


print (max_prime)