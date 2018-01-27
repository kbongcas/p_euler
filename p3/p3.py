"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

import math

# google says go up to square root of number
# an factor above the square root is going to be the pair of somehting smaller
# Ex. 24
# 5 * 5 will be over

def get_factors(number_to_check):
    "get factors of a number"
    factors = []
    for num in range(1, int(math.sqrt(number_to_check) + 1)):
        if number_to_check % num == 0:
            factors.append(num)
            factors.append(number_to_check // num)
    return factors


def get_prime_numbers(numbers):
    "get the prime factors"
    prim_nums = []
    for i in numbers:
        if isPrime(i):
            prim_nums.append(i)

    return prim_nums


def isPrime(number):
    "used get_factors of a number has no"
    if len(get_factors(number)) == 2:
        return True
    
    return False


def get_largest(numbers):
    "find the largest number"
    largest = 0
    if len(numbers) == 0:
        return None
    else:
        for i in numbers:
            if i > largest:
                largest = i
    return largest


print(get_largest(get_prime_numbers(get_factors(600851475143))))
