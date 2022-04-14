from functools import reduce


def calculate_score(sum_group, product_group):
    s = sum(sum_group)
    p = reduce(lambda acc, i: acc * i, product_group, 1)
    return s if s == p else 0


def prime_time(primes):
    n = len(primes)
    max_score = 0
    for i in range(1, 2 ** n - 1):
        first_group = [primes[x] for x in range(n) if i >> x & 1]
        second_group = [primes[x] for x in range(n) if not (i >> x & 1)]

        score1 = calculate_score(first_group, second_group)
        score2 = calculate_score(second_group, first_group)

        max_score = max(max_score, score1, score2)

    return max_score


def main():
    t = int(input())

    for c in range(1, t + 1):
        m = int(input())

        primes = list()
        for _ in range(m):
            p, n = [int(i) for i in input().split(' ')]
            primes += [p] * n

        sol = prime_time(primes)
        print('Case #{}: {}'.format(c, sol))


main()
