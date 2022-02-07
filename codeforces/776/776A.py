import sys


candidates = sys.stdin.readline().strip().split(' ', 2)
n = int(sys.stdin.readline().strip())
killed = []
candidates_list = [candidates]

for i in range(n):
    names = sys.stdin.readline().strip().split(' ', 2)
    new_candidates = list(candidates_list[-1])
    new_candidates.remove(names[0])
    new_candidates.append(names[1])
    candidates_list.append(new_candidates)

for candidates in candidates_list:
    print(f'{candidates[0]} {candidates[1]}')

