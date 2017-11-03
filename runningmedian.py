import sys
from heapq import heappush, heappop

class MinHeap(object):
    def __init__(self):
        self.h = []

    def push(self, x):
        heappush(self.h, x)

    def size(self):
        return len(self.h)

    def pop(self):
        return heappop(self.h)

    def peep(self):
        return self.h[0]

class MaxHeap(object):
    def __init__(self):
        self.h = []

    def push(self, x):
        heappush(self.h, -1 * x)

    def size(self):
        return len(self.h)

    def pop(self):
        return -1 * heappop(self.h)

    def peep(self):
        return -1 * self.h[0]

class RunningMedian(object):
    """
    Maintain self.maxh.size() >= self.minh.size()
    """
    def __init__(self):
        self.minh = MinHeap()
        self.maxh = MaxHeap()
        self.sum = 0

    def append(self, x):
        if self.maxh.size() == 0: 
            self.maxh.push(x)

        elif self.minh.size() == 0: 
            self.minh.push(x)

        elif self.minh.size() == self.maxh.size():
            # append to self.maxh
            if x < self.maxh.peep():
                self.maxh.push(x)
            elif x > self.minh.peep():
                self.minh.push(x)
                x = self.minh.pop()
                self.maxh.push(x)
            else:
                self.maxh.push(x)
        else:
            # append to self.minh
            if x < self.maxh.peep():
                self.maxh.push(x)
                x = self.maxh.pop()
                self.minh.push(x)
            elif x > self.minh.peep():
                self.minh.push(x)
            else:
                self.minh.push(x)

        self.sum += self.getMedian()

    def getMedian(self):
        return self.maxh.peep()

    def getSumOfMedians(self):
        return self.sum

def runningmedian():
    s = rl().strip().split(' ')
    n = int(s[0])
    a = int(s[1])
    b = int(s[2])

    l = RunningMedian()
    x = 1983
    l.append(x)
    for i in range(n-1):
        x = ( x * a + b ) % 20090711
        l.append(x)

    print l.getSumOfMedians() % 20090711



rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    runningmedian()
