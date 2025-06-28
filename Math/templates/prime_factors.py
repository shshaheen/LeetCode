INT_MAX = 10002
spf = list(range(INT_MAX))
for i in range(2, int(INT_MAX ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, INT_MAX, i):
            if spf[j] == j:
                spf[j] = i

def prime_factors(num):
    if num == 1:
        return [1]
    factors = []
    while num != 1:
        factors.append(spf[num])
        num //= spf[num]
    return factors
