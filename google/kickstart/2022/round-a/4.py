from math import log10


memo = {}


def count_digits(n):
    if n == 0:
        return 1

    return int(log10(n)) + 1


def get_digit(n, i):
    l = count_digits(n)
    return n // 10**(l - i - 1) % 10


def count_with_length(l, p = 1, s = 0, first_digit = False):
    if l == 0:
        return 1 if s > 0 and p % s == 0 else 0

    if (l, p, s) in memo:
        return memo[(l, p, s)]

    start_digit = 1 if first_digit else 0

    count = 0
    for digit in range(start_digit, 10):
        count += count_with_length(l - 1, p * digit, s + digit)

    memo[(l, p, s)] = count
    return memo[(l, p, s)]


def count_with_prefix(n, p = 1, s = 0, index = 0, first_digit = False):
    if index == count_digits(n):
        return 1 if s > 0 and p % s == 0 else 0

    start_digit = 1 if first_digit else 0
    l = count_digits(n) - index - 1
    current_digit =  get_digit(n, index)
    count = 0
    for digit in range(start_digit, current_digit):
        count += count_with_length(l, p * digit, s + digit)

    count += count_with_prefix(n, p * current_digit, s + current_digit, index + 1)

    return count


def count_up_to(n):
    l = count_digits(n)
    count = 0

    for i in range(1, l):
        count += count_with_length(i, first_digit = True)

    count += count_with_prefix(n, first_digit = True)

    return count


def interesting(a, b):
    count_a = count_up_to(a - 1)
    count_b = count_up_to(b)
    return count_b - count_a


def main():
    t = int(input())

    for c in range(1, t + 1):
        a, b = [int(i) for i in input().split(' ')]
        sol = interesting(a, b)
        print('Case #{}: {}'.format(c, sol))


main()
