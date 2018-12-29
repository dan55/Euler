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


def main():
    args = [3, 5]

    # the test case
    assert sum(brute_force(10, *args)) == 23

    # the problem
    print(sum(brute_force(1000, *args)))


if __name__ == "__main__":
    main()
