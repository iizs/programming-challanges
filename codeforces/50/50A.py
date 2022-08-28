import sys


values = sys.stdin.readline().strip().split(' ')
m = int(values[0])
n = int(values[1])

num = n * int(m/2)
if m % 2 == 1:
    num += int(n/2)
print(num)
