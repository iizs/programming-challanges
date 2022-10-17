import sys


nq = int(sys.stdin.readline().strip())

for i in range(nq):
    n = int(sys.stdin.readline().strip())
    array = sys.stdin.readline().strip().split()
    a = [int(e) for e in array]
    print(a)

