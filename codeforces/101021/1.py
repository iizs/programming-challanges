# https://codeforces.com/gym/101021/problem/1
import sys

minN = 1
maxN = 1000000
while minN < maxN:
    guess = int((minN + maxN) / 2)
    print(guess)
    sys.stdout.flush()
    ret = sys.stdin.readline().strip()
    if ret == '<':
        maxN = guess - 1
    elif ret == '<=':
        maxN = guess
    elif ret == '>':
        minN = guess + 1
    elif ret == '>=':
        minN = guess

print(f'! {maxN}')
