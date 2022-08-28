import sys


def find_recolor_num(pixels):
    pixels = ''.join(sorted(pixels))
    d = {}
    for c in pixels:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    print(len(d)-1)


nq = sys.stdin.readline().strip()
n = int(nq.split()[0])

for i in range(n):
    pixels = sys.stdin.readline().strip()
    pixels += sys.stdin.readline().strip()
    find_recolor_num(pixels)

"""
"""