from math import pi


def calc_area(r):
    return pi * r * r


def infinity_area(r, a, b):
    area = 0
    left = True

    while r > 0:
        area += calc_area(r)
        r = r * a if left else r // b
        left = not left

    return area


def main():
    t = int(input())

    for c in range(1, t + 1):
        r, a, b = [int(i) for i in input().split(' ')]
        sol = infinity_area(r, a, b)
        print('Case #{}: {}'.format(c, sol))


main()
