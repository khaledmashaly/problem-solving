# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a3a5

def print_sol(c, sol):
    print('Case #{}: {}'.format(c, sol))


def solve(n, a):
    seq = []

    start = None
    end = None
    d = None
    ans = 1
    for i in range(1, n):
        if a[i] - a[i - 1] != d:
            if start is not None:
                seq.append((start, end, d))
                ans = max(ans, end - start + 1)
            start = i - 1
            end = i
            d = a[i] - a[i - 1]
        else:
            end = i

    seq.append((start, end, d))
    ans = max(ans, end - start + 1)

    if ans == n:
        return ans

    ans += 1

    for (s, e, d) in seq:
        if s > 1 and a[s] - 2 * d == a[s - 2]:
            ans = max(ans, e - s + 3)
        if e < n - 2 and a[e] + 2 * d == a[e + 2]:
            ans = max(ans, e - s + 3)

    if len(seq) > 3:
        for i in range(3, len(seq)):
            s1, e1, d1 = seq[i]
            s2, e2, d2 = seq[i - 3]
            if d1 == d2 and a[s1] == a[e2] + 2 * d2:
                l1 = e1 - s1 + 1
                l2 = e2 - s2 + 1
                ans = max(ans, l1 + l2 + 1)

    return ans

def main():
    t = int(input())

    for c in range(1, t + 1):
        n = int(input())
        a = [int(i) for i in input().split(' ')]
        sol = solve(n, a)
        print_sol(c, sol)


if __name__ == '__main__':
    main()
