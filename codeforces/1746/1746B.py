import sys


def sort(l):
    cnt = 0
    idx_i = 0
    idx_j = len(l) - 1

    while idx_j > 0 and l[idx_j] == 1:
        idx_j -= 1
    while idx_i < idx_j:
        if l[idx_i] == 0:
            idx_i += 1
            continue
        else:
            e = l.pop(idx_i)
            idx_j -= 1
            l[idx_j] += e
            cnt += 1
            while idx_j > 0 and l[idx_j] == 1:
                idx_j -= 1
    # print(l)
    return cnt


nq = int(sys.stdin.readline().strip())

for i in range(nq):
    n = int(sys.stdin.readline().strip())
    array = sys.stdin.readline().strip().split()
    a = [int(e) for e in array]
    # print(a)
    print(sort(a))




