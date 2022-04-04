class Printer:
    def __init__(self, c, m, y, k):
        self.c = c
        self.m = m
        self.y = y
        self.k = k


def printing(printers):
    units_remaining = 10 ** 6

    color = [0] * 4

    c_min = min(printer.c for printer in printers)
    m_min = min(printer.m for printer in printers)
    y_min = min(printer.y for printer in printers)
    k_min = min(printer.k for printer in printers)

    colors_min = [c_min, m_min, y_min, k_min]

    for i in range(4):
        if units_remaining > 0:
            color[i] += min(colors_min[i], units_remaining)
            units_remaining -= color[i]

    return color if units_remaining == 0 else []


def main():
    t = int(input())

    for x in range(1, t + 1):
        printers = list()
        for i in range(3):
            c, m, y, k = [int(a) for a in input().split(' ')]
            printer = Printer(c, m, y, k)
            printers.append(printer)

        color = printing(printers)
        sol = ' '.join(str(i) for i in color) if color else 'IMPOSSIBLE'
        print('Case #{}: {}'.format(x, sol))


main()
