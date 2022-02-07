import sys


def abbr(s):
    return s[0] + str(len(s) - 2) + s[-1]


n = int(sys.stdin.readline().strip())

for i in range(n):
    word = sys.stdin.readline().strip()
    if len(word) > 10:
        print(abbr(word))
    else:
        print(word)
