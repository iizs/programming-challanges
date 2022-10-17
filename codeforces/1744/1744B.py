import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    nq = sys.stdin.readline().strip().split()
    n = int(nq[0])
    q = int(nq[1])
    array_line = sys.stdin.readline().strip().split()
    sum_a = 0
    count_odd = 0
    count_even = 0
    for e in array_line:
        en = int(e)
        sum_a += en
        if en % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    for qn in range(q):
        query = sys.stdin.readline().strip().split()
        x = int(query[1])
        if query[0] == '0':
            # even
            sum_a += count_even * x
            if x % 2 == 1:
                count_odd += count_even
                count_even = 0
        elif query[0] == '1':
            sum_a += count_odd * x
            if x % 2 == 1:
                count_even += count_odd
                count_odd = 0
        print(sum_a)




