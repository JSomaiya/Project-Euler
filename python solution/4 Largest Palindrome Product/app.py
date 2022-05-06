'''
Project Euler Challenge 04. Largest Palindrome Product

Problem Question:
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

largest = 0

for n1 in range(100, 999):
    for n2 in range (100, 999):
        p1 = n1 * n2
        p1s = str(p1)
        if p1s == p1s[::-1]:
            if p1 > largest:
                largest = p1

print (largest)