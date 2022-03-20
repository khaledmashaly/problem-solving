def rd_int():
    return int(input())


def rd_str():
    return input()


def print_sol(c, sol):
    print('Case #{}: {}'.format(c, sol))


def speed_typing(i: str, p: str) -> str:
    if len(i) > len(p):
        return 'IMPOSSIBLE'

    x = y = 0
    while x < len(i) and y < len(p):
        if i[x] == p[y]:
            x += 1
        y += 1

    if x != len(i):
        return 'IMPOSSIBLE'

    return str(len(p) - len(i))


def main():
    t = rd_int()

    for c in range(1, t + 1):
        i = rd_str()
        p = rd_str()
        sol = speed_typing(i, p)
        print_sol(c, sol)


if __name__ == '__main__':
    main()
