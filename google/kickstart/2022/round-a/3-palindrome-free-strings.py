def print_sol(c, sol):
    print('Case #{}: {}'.format(c, sol))


def is_valid(s: str) -> bool:
    n = len(s)

    if n < 5:
        return True

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return True

    return False


def palindrome_free_strings(n: int, s: str) -> str:
    if n < 5:
        return 'POSSIBLE'

    current_level = set([''])
    i = 0
    while current_level and i < n:
        next_level = set()
        for prefix in current_level:
            if s[i] == '?':
                zero = prefix + '0'
                if is_valid(zero[-6:]) and is_valid(zero[-5:]):
                    next_level.add(zero[-5:])
                one = prefix + '1'
                if is_valid(one[-6:]) and is_valid(one[-5:]):
                    next_level.add(one[-5:])
            else:
                next_prefix = prefix + s[i]
                if is_valid(next_prefix[-6:]) and is_valid(next_prefix[-5:]):
                    next_level.add(next_prefix[-5:])
        current_level = next_level
        i += 1

    valid = current_level and i == n
    return 'POSSIBLE' if valid else 'IMPOSSIBLE'


def main():
    t = int(input())

    for c in range(1, t + 1):
        n = int(input())
        s = input()
        sol = palindrome_free_strings(n, s)
        print_sol(c, sol)


if __name__ == '__main__':
    main()
