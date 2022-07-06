import sys


values = sys.stdin.readline().strip().split(' ')
m = int(values[0])
n = int(values[1])

num = int(n * m / 2)

print(num)
