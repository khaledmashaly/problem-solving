def punch_cards(r, c):
    row_sep = '+-'
    row_data = '|.'
    first_row_sep = '..' + row_sep * (c - 1) + '+'
    first_row_data = '..' + row_data * (c - 1) + '|'
    print(first_row_sep)
    print(first_row_data)

    for i in range(r - 1):
        print(row_sep * c + '+')
        print(row_data * c + '|')

    print(row_sep * c + '+')


def main():
    t = int(input())

    for a in range(1, t + 1):
        r, c = [int(x) for x in input().split(' ')]
        print('Case #{}:'.format(a))
        punch_cards(r, c)


main()
