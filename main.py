import time
from functools import wraps
import argparse


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"\nExecution time of {func.__name__}: {end - start:.5f} seconds")
            wrapper.has_run = False
            return result
        else:
            return func(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


@timer
def fibonacci(n, memo={}):
    """
    Find Fibonacci of a given number using memoization

    :param n: given number
    :param memo:internal use for memoization.
    """
    # print(f"Value of memo dict: {memo}")

    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


@timer
def fibonacci_no_memo(n):
    """
    Find Fibonacci of a given number

    :param n: given number

    """
    if n <= 2:
        return 1
    return fibonacci_no_memo(n - 1) + fibonacci_no_memo(n - 2)


if __name__ == "__main__":
    """
    Command Line argument --num n

    """
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-p", "--num", help="Enter Number")

    args = argParser.parse_args()
    n = int(args.num)

    print("\n USING MEMOIZATION")

    print(
        f"\nCalculating Fibonacci of {n} for the first time with memoization:",
        fibonacci(n),
    )
    print(
        f"\nCalculating Fibonacci of {n} for the second time with memoization:",
        fibonacci(n),
    )

    print("\n\n WITHOUT MEMOIZATION")

    print(
        f"\n\nCalculating Fibonacci of {n} for the first time without memoization:",
        fibonacci_no_memo(n),
    )
    print(
        f"\nCalculating Fibonacci of {n} for the second time without memoization:",
        fibonacci_no_memo(n),
    )
