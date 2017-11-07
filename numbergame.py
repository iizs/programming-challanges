import sys

rl = lambda: sys.stdin.readline()

def findBest(l, gap):
    gap = -1 * gap;

    if len(l) == 0:
        return -1 * gap
    elif len(l) == 1:
        return -1 * ( gap + l[0] )

    # 1.1 get left most value
    c_gap = findBest( l[1:],  gap + l[0] )
    n_gap = c_gap
    # 1.2 get right most value
    c_gap = findBest( l[:-1], gap + l[-1] )
    if n_gap < c_gap:
        n_gap = c_gap
    # 2.1 remove left 2 values
    c_gap = findBest( l[2:],  gap )
    if n_gap < c_gap:
        n_gap = c_gap
    # 2.2 remove right 2 values
    c_gap = findBest( l[:-2],  gap )
    if n_gap < c_gap:
        n_gap = c_gap

    return -1 * n_gap

# main
n_sets = int(rl())

for i in range(n_sets):
    n_nums = int(rl())
    l_nums = [int(s) for s in rl().strip().split(' ')[0:n_nums]]
    print -1 * findBest(l_nums, 0)
