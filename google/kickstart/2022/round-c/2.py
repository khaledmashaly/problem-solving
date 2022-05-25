# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20deb

def partition_sum(n, x, y):    
    n_sum = int(n / 2 * (1 + n))

    if n_sum % (x + y) != 0:
        return None

    return int(n_sum * x / (x + y))


def partition_set(n, a):
    s = set()
    s_sum = 0

    for i in reversed(range(1, n + 1)):
        if s_sum == a:
            break

        if s_sum + i <= a:
            s.add(i)
            s_sum += i

    return s


def range_partition(n, x, y):
    a = partition_sum(n, x, y)
    return partition_set(n, a) if a is not None else None


def main():
    t = int(input())

    for c in range(1, t + 1):
        n, x, y = [int(i) for i in input().split(' ')]
        sol = range_partition(n, x, y)
        if sol is not None:
            print('Case #{}: POSSIBLE'.format(c))
            print(len(sol))
            print(*sol)
        else:
            print('Case #{}: IMPOSSIBLE'.format(c))


main()
