from math import sqrt


def sieve(n: int) -> list[bool]:
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    
    return prime
