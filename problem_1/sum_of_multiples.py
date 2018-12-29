"""
Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""


def brute_force(n, *args):
    """
    Yield all of the numbers between 1 and n that are divisible by any of the other args
    """

    for i in range(1, n):
        if any([arg for arg in args if i % arg == 0]):
            yield i


if __name__ == "__main__":
    # the test case
    assert sum(brute_force(10, 3, 5)) == 23

    # the problem
    print(sum(brute_force(1000, 3, 5)))
