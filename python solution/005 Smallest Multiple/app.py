'''
Project Euler Challenge 05: Smallest Multiple

Problem Question:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
smallest = 1
current = 1
while True:
    counter = 0
    for n in range (1, 21):
        if current % n == 0:
            counter += 1

    if counter == 20:
        smallest = current
        break
    
    current += 1
print (smallest)
