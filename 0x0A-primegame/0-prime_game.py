#!/usr/bin/python3
"""Maria and Ben prime game"""


def isWinner(x, nums):
    if x <= 0 or nums is None:
        return None

    def sieve_of_eratosthenes(limit):
        """finds all primes upto """
        primes = []
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for number, prime in enumerate(is_prime):
            if prime:
                primes.append(number)
                for multiple in range(number * number, limit + 1, number):
                    is_prime[multiple] = False
        return primes

    def can_win(n):
        primes = sieve_of_eratosthenes(n)
        memo = {}

        def can_win_recursive(remaining):
            if remaining == 0:
                return False

            if remaining in memo:
                return memo[remaining]

            for prime in primes:
                if prime > remaining:
                    break
                if not can_win_recursive(remaining - prime):
                    memo[remaining] = True
                    return True

            memo[remaining] = False
            return False

        return can_win_recursive(n)

    maria = 0
    ben = 0

    for n in nums:
        if can_win(n):
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
