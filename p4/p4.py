# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# 999 x 999  most 6 digits 
# 999 x 999 

import math

digits = 3

def isPalindorome(s):
    # reverse is the same 
    if str(s) == str(s)[::-1]:
        return True
    else:
        return False


def findLargestPal(digits):
    # start at largest
    highest_number = int((math.pow(10, digits)))
    largest_pal = -1

    
    # loop through all possible factors and check if product is palindrome
    for i in reversed(range(1, highest_number)):
        for j in reversed(range(1, highest_number)):
            product = i * j
            if isPalindorome(product) and product > largest_pal:
                largest_pal = product
    
    ## once done check if there was a palindrome
    if largest_pal == -1:
        return None
    else:
        return largest_pal

print(findLargestPal(digits))
