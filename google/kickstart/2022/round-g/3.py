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


def solve(n, a):
    s = 0
    for i in range(n):
        ps = 0
        ls = 0
        for j in range(i, n):
            ps += a[j]
            if ps >= 0:
                ls += ps
            else:
                break
        s += ls
    return s


def main():
    t = rd_int()

    for c in range(1, t + 1):
        n = rd_int()
        a = rd_int_lst()

        sol = solve(n, a)
        print_sol(c, sol)

if __name__ == '__main__':
    main()
