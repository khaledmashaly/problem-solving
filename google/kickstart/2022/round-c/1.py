# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20f15
from re import search


def new_password(n, old_password):
    sol = old_password

    # upper
    if search('[A-Z]', old_password) is None:
        sol += 'A'

    # lower
    if search('[a-z]', old_password) is None:
        sol += 'a'

    # digit
    if search('[0-9]', old_password) is None:
        sol += '0'

    # special
    if search('[#@*&]', old_password) is None:
        sol += '#'

    # length
    if len(sol) < 7:
        sol += 'a' * ( 7 - len(sol))

    return sol


def main():
    t = int(input())

    for c in range(1, t + 1):
        n = int(input())
        old_password = input()
        sol = new_password(n, old_password)
        print('Case #{}: {}'.format(c, sol))


main()
