# Smallest multiple
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?



def remove_redundant_nums(divisors):
    """ Removes the redundant divisors,
        Ex. if a number can be divided
        by 20 then it can also be divide by 10
    """

    redundant_nums = []

    # sort the divisors
    divisors.sort()

    # see if any divisor can be divided by another divisor
    for divisor in reversed(divisors):
        for another_divisor in divisors:
            print("{} % {} = {}".format(divisor,
                                        another_divisor,
                                        divisor % another_divisor))
            if divisor != another_divisor and divisor % another_divisor == 0:
                redundant_nums.append(another_divisor)

    # remove the redundant numbers
    for redundant_num in redundant_nums:
        print("redundant_num = {}".format(redundant_num))
        if redundant_num in divisors:
            divisors.remove(redundant_num)

    print(divisors)
    return divisors


def number_is_divisible(number, divisors):
    """ Checks if a number is divisible given a set of divisors, must
        be divisible by all divisors to return true
    """

    for divisor in divisors:
        if number % divisor != 0:
            return False

    return True


def find_smallest_num(divisors):
    """ Find the smallest number that is divisible by all given divisors.
    """

    smallest_divisor = min(divisors)
    current_count = smallest_divisor
    while True:
        current_count = current_count + smallest_divisor
        if number_is_divisible(current_count, divisors):
            break

    return current_count


TEST_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

REFIND_ARRAY = remove_redundant_nums(TEST_ARRAY)
print(find_smallest_num(REFIND_ARRAY))
