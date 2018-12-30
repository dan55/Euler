"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

https://projecteuler.net/problem=2
"""


def generate_fib_seq(a=1, b=2, max_val=100, divisible_by=1):
    """ Generate terms of the sequence that are divisible by divisible_by
        and whose maximum value does not exceed max_val, starting at a and b
    """

    while a < max_val:
        if a % divisible_by == 0:
            yield a
        a, b = b, a + b


def brute_force():
    """ A brute force solution to the problem """

    return sum(generate_fib_seq(max_val=4000000, divisible_by=2))


def main():
    # test of the basic sequence, as outlined in the problem statement
    assert list(generate_fib_seq()) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # test of generating only the even numbers in the sequence
    assert list(generate_fib_seq(divisible_by=2)) == [2, 8, 34]

    print(brute_force())


if __name__ == "__main__":
    main()
