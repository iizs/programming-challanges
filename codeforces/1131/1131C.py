import sys


n = int(sys.stdin.readline().strip())

heights = [int(i) for i in sys.stdin.readline().strip().split(' ', n)]

heights = list(sorted(heights))

left = []
right = []

for i in heights:
    if len(left) == len(right):
        left.append(i)
    else:
        right.append(i)

answer = list(left)
answer.extend(reversed(right))

print(' '.join([str(c) for c in answer]))
