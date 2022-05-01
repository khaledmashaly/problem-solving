from math import sqrt


def is_palindromic(i):
    s = str(i)
    for x in range(len(s) // 2):
        if s[x] != s[len(s) - x - 1]:
            return False
    return True


def palindromic_factors(a):
    ans = 0
    for i in range(1, int(sqrt(a)) + 1):
        if a % i == 0:
            if is_palindromic(i):
                ans += 1
            j = a // i
            if i != j and is_palindromic(j):
                ans += 1
    return ans


def main():
    t = int(input())

    for c in range(1, t + 1):
        a = int(input())
        sol = palindromic_factors(a)
        print('Case #{}: {}'.format(c, sol))


main()
