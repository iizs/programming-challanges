import sys


def able_to_fill(list_a, list_b, a, b):
    a_skipped = False
    b_skipped = False
    a_idx = 0
    b_idx = 0
    while a_idx < len(list_a) and b_idx < len(list_b):
        if not a_skipped and a == list_a[a_idx]:
            a_idx += 1
            a_skipped = True
            continue
        if not b_skipped and b == list_b[b_idx]:
            b_idx += 1
            b_skipped = True
            continue
        if list_a[a_idx] > list_b[b_idx]:
            return False
        a_idx += 1
        b_idx += 1
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
