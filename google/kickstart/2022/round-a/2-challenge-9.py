from functools import reduce


def print_sol(c, sol):
    print('Case #{}: {}'.format(c, sol))


def challenge_9(n: str):
    sum_mod_9 = lambda a, b: (a + b) % 9
    mod = reduce(lambda acc, cur: sum_mod_9(acc, ord(cur) - ord('0')), n, 0)
    d = str(9 - mod)

    if d == '9':
        return n[0] + '0' + n[1:]

    for i in range(len(n)):
        if d < n[i]:
            return n[:i] + d + n[i:]

    return n + d


def main():
    t = int(input())

    for c in range(1, t + 1):
        n = input()
        sol = challenge_9(n)
        print_sol(c, sol)


if __name__ == '__main__':
    main()
