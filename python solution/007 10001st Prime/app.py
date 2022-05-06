'''
Project Euler Challenge 07 10 001st Prime

Problem Question:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

num = 2
prime = 0
while True:
    counter = 0

    for a in range(2, num+1):
        if num % a == 0:
            counter += 1
            continue
    

    if counter < 2:
        prime += 1
        
    
    if (prime == 10001):
        print(num)
        break

    num += 1
