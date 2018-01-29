# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?


def find_ith_prime(ith):
    """ find the prime number that is the ith element in a list of ordered
    prime numbers
    """
    count = 2
    prime_count = 0
    ith_prime = 0

    while prime_count < ith:
        print("Check if {} is prime".format(count))
        if all(count % i for i in range(2, count)):
            ith_prime = count
            prime_count = prime_count + 1
            print("True")
            print("Prime count = " + str(prime_count))
        else:
            print("False")
        count = count + 1
    return ith_prime


print(find_ith_prime(10001))
