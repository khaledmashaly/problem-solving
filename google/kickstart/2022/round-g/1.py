def rd_int():
    return int(input())


def rd_str():
    return input()


def rd_str_lst():
    return input().split(' ')


def sp_str_lst():
    return list(input())


def rd_int_lst():
    return [int(i) for i in rd_str_lst()]


def sp_int_lst():
    return [int(i) for i in sp_str_lst()]


def print_sol(c, sol):
    print('Case #{}: {}'.format(c, sol))


def solve(m, n, p, s):
    john = s[p - 1]
    sol = [0] * n

    for i in range(m):
        for j in range(n):
            sol[j] = max(sol[j], s[i][j] - john[j])

    return sum(sol)


def main():
    t = rd_int()

    for c in range(1, t + 1):
        m, n, p = rd_int_lst()
        s = [[0] * n for _ in range(m)]

        for i in range(m):
            s[i] = rd_int_lst()

        sol = solve(m, n, p, s)
        print_sol(c, sol)


if __name__ == '__main__':
    main()
