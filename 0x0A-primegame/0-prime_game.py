#!/usr/bin/python3
"""Maria and Ben prime game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    prime = [1 for x in range(sorted(nums)[-1] + 1)]
    prime[0], prime[1] = 0, 0
    for i in range(2, len(prime)):
        rm_multiples(prime, i)

    for i in nums:
        if sum(prime[0:i + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
