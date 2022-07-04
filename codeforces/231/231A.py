import sys


n = int(sys.stdin.readline().strip())
count = 0
approved = 0

while count < n:
    line = sys.stdin.readline()
    votes = [int(v) for v in line.strip().split(' ')]
    pro = sum(votes)
    if pro >= 2:
        approved += 1
    count += 1

print(approved)
