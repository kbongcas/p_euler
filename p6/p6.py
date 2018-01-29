#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^22 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def sum_of_squares(the_max):
    """ Find the sum of squares."""
    count = 0
    for i in range(1, the_max + 1):
        count = count + (i * i)
        print(" {} = {} + ({} * {})".format(count, count, i, i))
    return count


def square_of_sum(the_max):
    """Find the square of sums."""
    count = 0
    for i in range(1, the_max + 1):
        count = count + i
        print(" {} = {} + {}".format(count, count, i))
    return count * count


SUM_ONE = sum_of_squares(100)
SUM_TWO = square_of_sum(100)

print("Sum of Squares: " + str(SUM_ONE))
print("Square of Sums: " + str(SUM_TWO))
print("The difference between the sum of squares: " + str(SUM_TWO - SUM_ONE))
