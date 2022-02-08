import sys


def board_moves(size):
    if size == 1:
        return 0
    sum = 0
    prev = 1
    prev_2 = prev * prev
    for cur in range(3, size+1, 2):
        q = cur // 2
        cur_2 = cur * cur
        sum += (cur_2 - prev_2) * q
        prev_2 = cur_2
    return sum


t = int(sys.stdin.readline().strip())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    print(board_moves(n))
