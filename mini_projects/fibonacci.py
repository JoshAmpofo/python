# memoization
from typing import Dict
# create memo base cases
memo: Dict[int, int] = {0: 0, 1: 1}

def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2) # memoization
    return memo[n]


if __name__ == '__main__':
    print(fib(5))
    print(fib(50))


