import sys


def able_to_fill(list_a, list_b, a, b):
    l_a = list(list_a)
    l_b = list(list_b)
    l_a.remove(a)
    l_b.remove(b)
    for (item_a, item_b) in zip(l_a, l_b):
        if item_a > item_b:
            return False
    return True


n = int(sys.stdin.readline().strip())

for i in range(n):
    size = int(sys.stdin.readline().strip())
    list_a = [int(c) for c in sys.stdin.readline().strip().split()]
    list_b = [int(c) for c in sys.stdin.readline().strip().split()]
    list_d_min = []
    prev_a = None
    prev_d = None
    for a in list_a:
        if prev_a is not None and prev_a == a:
            list_d_min.append(prev_d)
            continue
        for b in list_b:
            if b >= a:
                list_d_min.append(b - a)
                prev_a = a
                prev_d = b - a
                break

    # Warning. lists will be in revered form
    list_d_max = []
    list_a.reverse()
    list_b.reverse()
    prev_a = None
    prev_d = None
    for a in list_a:
        if prev_a is not None and prev_a == a:
            list_d_max.append(prev_d)
            continue
        for b in list_b:
            if able_to_fill(list_a, list_b, a, b):
                list_d_max.append(b - a)
                prev_a = a
                prev_d = b - a
                break

    list_d_max.reverse()
    # print(list_a)
    # print(list_b)
    print(' '.join([str(s) for s in list_d_min]))
    print(' '.join([str(s) for s in list_d_max]))
