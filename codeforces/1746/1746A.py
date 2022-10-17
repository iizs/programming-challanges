import sys


nq = sys.stdin.readline().strip()
n = int(nq.split()[0])

for i in range(n):
    nk_line = sys.stdin.readline().strip()
    array_a_line = sys.stdin.readline().strip()
    (n, k) = nk_line.split()
    array_a = array_a_line.split()
    has_1 = False
    for e in array_a:
        if e == '1':
            has_1 = True
            break

    if has_1:
        print("YES")
    else:
        print("NO")


