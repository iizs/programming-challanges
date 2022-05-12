# https://codeforces.com/problemset/problem/1443/E
# passed 4 test, failed 5th test
import sys

factorials = {0: 1, 1: 1}


def factorial(n):
    if n not in factorials:
        k = max(factorials.keys())
        while k < n:
            factorials[k + 1] = factorials[k] * (k + 1)
            k += 1

    return factorials[n]


class Permutation:
    def __init__(self, size, elements=None):
        if elements is None:
            self.elements = [i for i in range(1, size+1)]
        else:
            self.elements = sorted(elements)
        self.permutation = list(self.elements)
        self.last_idx = [0 for i in range(1, size+1)]
        self.sum_total = 0
        for i in self.elements:
            self.sum_total += i

    def __str__(self):
        return str(self.permutation)

    # base 1
    def get_nth(self, n):
        elements = list(self.elements)
        base = 0
        use_last_index = True
        len_remain_elements = len(elements)
        for o in range(0, len_remain_elements):
            idx = self.last_idx[o] if use_last_index else 0
            while True:
                if base + (idx + 1) * factorial(len_remain_elements-1) >= n:
                    break
                idx += 1
                use_last_index = False
            self.last_idx[o] = idx
            base += idx * factorial(len_remain_elements-1)
            num = elements[idx]
            self.permutation[o] = num
            elements.remove(num)
            len_remain_elements -= 1
        return self.permutation

    def sum(self, a, b):
        if b - a < len(self.elements)/2:
            s = 0
            for i in range(a, b+1):
                s += self.permutation[i-1]
        else:
            s = self.sum_total
            for i in range(1, a):
                s -= self.permutation[i-1]
            for i in range(b+1, len(self.elements)+1):
                s -= self.permutation[i-1]

        return s


nq = sys.stdin.readline().strip()
n = int(nq.split()[0])
q = int(nq.split()[1])

p = Permutation(n)
idx = 1
need_update = False
for i in range(q):
    cmd = sys.stdin.readline().strip()
    cmds = cmd.split()
    if cmds[0] == '1':
        if need_update:
            p.get_nth(idx)
            need_update = False
        print(p.sum(int(cmds[1]), int(cmds[2])))
    elif cmds[0] == '2':
        idx += int(cmds[1])
        need_update = True

    else:
        continue
