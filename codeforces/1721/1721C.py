import sys


n = int(sys.stdin.readline().strip())

for i in range(n):
    size = int(sys.stdin.readline().strip())
    list_a = [int(c) for c in sys.stdin.readline().strip().split()]
    list_b = [int(c) for c in sys.stdin.readline().strip().split()]
    list_d_min = []
    for a in list_a:
        for b in list_b:
            if b >= a:
                list_d_min.append(b - a)
                break
    list_d_max = []
    for a in list_a:
        for b in list_b:
            if b >= a:
                list_d_min.append(b - a)
                break

    print(list_a)
    print(list_b)
    print(list_d_min)
    print(list_d_max)

"""
"""