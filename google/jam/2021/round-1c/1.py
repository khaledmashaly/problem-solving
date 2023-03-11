# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00

from math import ceil, floor


def print_sol(c, sol):
    print('Case #{}: {}'.format(c, sol))


def solve(n, k, p):
    p.sort()

    ranges = [p[0] - 1, k - p[-1]]
    for i in range(1, n):
        r = (p[i] - p[i - 1] - 1) / 2
        r1 = ceil(r)
        r2 = floor(r)
        ranges.append(r1)
        ranges.append(r2)

    ranges.sort()

    return (ranges[-1] + ranges[-2]) / k


def main():
    t = int(input())

    for c in range(1, t + 1):
        n, k = [int(i) for i in input().split(' ')]
        p = [int(i) for i in input().split(' ')]
        sol = solve(n, k, p)
        print_sol(c, sol)


if __name__ == '__main__':
    main()
