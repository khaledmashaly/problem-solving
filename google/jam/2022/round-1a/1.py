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


def solve(s: str):
    current_min = s[-1]
    for i in reversed(range(len(s) - 1)):
        double = s[i] * 2 + current_min
        not_double = s[i] + current_min
        current_min = double if double < not_double else not_double
    return current_min


def main():
    t = rd_int()

    for c in range(1, t + 1):
        s = rd_str()
        sol = solve(s)
        print_sol(c, sol)


if __name__ == '__main__':
    main()
