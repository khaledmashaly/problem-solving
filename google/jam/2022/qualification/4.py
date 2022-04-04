def rd_int():
    return int(input())


def rd_str_lst():
    return input().split(' ')


def rd_int_lst():
    return [int(i) for i in rd_str_lst()]


def print_sol(c, sol):
    print('Case #{}: {}'.format(c, sol))


class Node():
    def __init__(self, fun: int):
        self.fun = fun
        self.parent = None
        self.min_child_fun = 0
        self.total_children_fun = 0
        self.children = set()
        self.add_score = False


def chain_reaction(n, f, p):
    nodes = [Node(0)] + [Node(fi) for fi in f]

    for i in range(n):
        nodes[i + 1].parent = nodes[p[i]]
        nodes[p[i]].children.add(nodes[i + 1])
        if len(nodes[p[i]].children) > 1:
            nodes[p[i]].add_score = True

    nodes[0].add_score = True
    max_score = 0
    stack = [nodes[0]]
    while stack:
        current = stack[-1]
        for child in current.children:
            stack.append(child)
            current.children.remove(child)
            break
        else:
            current = stack.pop()
            if current.add_score:
                max_score += current.total_children_fun

            current.fun = max(current.fun, current.min_child_fun)
            parent = current.parent
            if parent:
                if parent.min_child_fun == 0 or current.fun < parent.min_child_fun:
                    parent.total_children_fun += parent.min_child_fun
                    parent.min_child_fun = current.fun
                else:
                    parent.total_children_fun += current.fun


    max_score += nodes[0].fun
    return max_score


def main():
    t = rd_int()

    for c in range(1, t + 1):
        n = rd_int()
        f = rd_int_lst()
        p = rd_int_lst()
        sol = chain_reaction(n, f, p)
        print_sol(c, sol)


if __name__ == '__main__':
    main()
