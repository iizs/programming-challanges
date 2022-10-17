import sys

def get_num_pow_2(n):
    r = 0
    while n > 1:
        if n % 2 == 0:
            r += 1
        else:
            break
        n = int(n / 2)
    return r


t = int(sys.stdin.readline().strip())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    array_line = sys.stdin.readline().strip().split()

    num_pow_2 = 0
    map_pow_2 = {}
    max_p = 0
    for idx in range(n):
        a = int(array_line[idx])
        num_pow_2 += get_num_pow_2(a)
        p = get_num_pow_2(idx+1)
        if p not in map_pow_2:
            map_pow_2[p] = 0
            max_p = p
        map_pow_2[p] += 1
    cnt = 0
    diff = n - num_pow_2
    while diff > 0 and max_p > 0:
        if diff - max_p >= 0:
            if map_pow_2[max_p] > 0:
                diff -= max_p
                cnt += 1
                map_pow_2[max_p] -= 1
            else:
                max_p -= 1
        else:
            max_p -= 1
    if diff <= 0:
        print(cnt)
    else:
        print(-1)





