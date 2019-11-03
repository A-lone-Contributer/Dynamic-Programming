# Fibonacci Numbers

# Find the nth fibonacci number.

# Fibonacci numbers, commonly denoted Fn form a sequence,
# called the Fibonacci sequence, such that each number is the sum
# of the two preceding ones, starting from 0 and 1.

# There are a lot of ways to find the fibonacci numbers but we will
# look at the DP approach here. It is not the most efficient as way available.


def nth_fib(n):

    # cache for lookup
    fib = {}

    # if given number is negative
    if n < 0:
        return -1

    # base case
    if n <= 1:
        return n

    else:

        # if the value is not already computed
        if n not in fib:

            # compute it and store it in fib[n]
            fib[n] = nth_fib(n - 1) + nth_fib(n - 2)

    # return the value
    return fib[n]


# Driver code
print(nth_fib(10))


# Time Complexity : O(n)
# Time Complexity : O(n)
