def print_sol(c, sol):
    print('Case #{}: {}'.format(c, sol))


def min_ops(l, r, c_sum, memo):
    if (l, r) in memo:
        return memo[(l, r)]

    if l == r:
        return 0

    sol = float('inf')
    for x in range(l, r):
        sol_left = min_ops(l, x, c_sum, memo) + 2 * (c_sum[l][x] - c_sum[l][r])
        sol_right = min_ops(x + 1, r, c_sum, memo) + 2 * (c_sum[x + 1][r] - c_sum[l][r])
        sol = min(sol, sol_left + sol_right)

    memo[(l, r)] = sol
    return memo[(l, r)]


def weightlifting(e, w, x):
    c = [[[0] * w for _ in range(e)] for _ in range(e)]
    c_sum = [[0] * e for _ in range(e)]

    for i in range(e):
        for j in range(w):
            c[i][i][j] = x[i][j]
            c_sum[i][i] += c[i][i][j]

    for l in range(e):
        for r in range(l + 1, e):
            for i in range(w):
                c[l][r][i] = min(c[l][r - 1][i], x[r][i])
                c_sum[l][r] += c[l][r][i]

    memo = {}
    return min_ops(0, e - 1, c_sum, memo) + 2 * c_sum[0][e - 1]


def main():
    t = int(input())

    for c in range(1, t + 1):
        e, w = [int(i) for i in input().split(' ')]

        x = [[0] * w for _ in range(e)]
        for i in range(e):
            x[i] = [int(i) for i in input().split(' ')]

        sol = weightlifting(e, w, x)
        print('Case #{}: {}'.format(c, sol))


if __name__ == '__main__':
    main()
