"""
This solution use the dynamic programming approach
with memoization for compute the fibonacci of a 
given number. This is an optimization for compute
the fibonacci of big numbers.
"""
def fib(n, memo={}):
    if n < 0:
        return "Error: n should be greater than zero"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


if __name__ == '__main__':
    n = 100
    print(f"Fibonacci of {n} is: {fib(n)}")