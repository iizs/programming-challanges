# -*- coding: utf-8 -*-
import math


def count_n_upto(n, to):
    cnt = 0
    p = int(math.log10(to))  # 자릿수
    dividend = to + 1

    for o in range(0, p + 1):
        divisor = 10 ** (o + 1)
        quotient_1 = dividend // divisor
        remainder_1 = dividend % divisor

        if o == 0:
            cnt += quotient_1
            if remainder_1 >= n + 1:
                cnt += 1
        else:
            quotient_2 = remainder_1 // 10 ** o
            remainder_2 = remainder_1 % 10 ** o
            cnt += quotient_1 * (10 ** o)
            if quotient_2 > n:
                cnt += 10 ** o
            elif quotient_2 == n:
                cnt += remainder_2

    return cnt


def count(n, a, b):
    if a == 0:
        return count_n_upto(n, b)
    return count_n_upto(n, b) - count_n_upto(n, a - 1)


"""
for line in sys.stdin:
    p = line.split(' ')
    print(count(int(p[2]), int(p[0]), int(p[1])))
"""
print(count_n_upto(1, 100))

for limit in range(1, 10000):
    cnt_dict = {num: 0 for num in range(0, 10)}
    for it in range(0, limit + 1):
        for char in str(it):
            cnt_dict[int(char)] += 1

    for num in range(1, 10):
        assert count_n_upto(num, limit) == cnt_dict[num], \
            f'{num}, {limit}: {count_n_upto(num, limit)} != {cnt_dict[num]}'
