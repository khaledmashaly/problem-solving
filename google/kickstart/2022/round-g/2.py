from math import sqrt


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


def calc_dist_min(rs, rh, centres):
    dist = []
    dist_min = float('inf')

    for i in range(len(centres)):
        d = sqrt(centres[i][0] ** 2 + centres[i][1] ** 2)
        if d <= rs + rh:
            dist.append(d)
            dist_min = min(dist_min, d)

    return dist, dist_min


def solve(rs, rh, n, m, red, yellow):
    red_dist, red_min = calc_dist_min(rs, rh, red)
    yellow_dist, yellow_min = calc_dist_min(rs, rh, yellow)

    red_score = [s < yellow_min for s in red_dist].count(True)
    yellow_score = [s < red_min for s in yellow_dist].count(True)

    return '{} {}'.format(red_score, yellow_score)


def main():
    t = rd_int()

    for c in range(1, t + 1):
        rs, rh = rd_int_lst()

        n = rd_int()
        red = [[0, 0] for _ in range(n)]
        for i in range(n):
            red[i] = rd_int_lst()

        m = rd_int()
        yellow = [[0, 0] for _ in range(m)]
        for j in range(m):
            yellow[j] = rd_int_lst()

        sol = solve(rs, rh, n, m, red, yellow)
        print_sol(c, sol)

if __name__ == '__main__':
    main()
