import sys

rl = lambda: sys.stdin.readline()

class Boggle:
    board = []
    cmap = {}
    fmap = {}

    def mk_fmap_key(self, point, word, cindex):
        return point+":"+word+":"+str(cindex)

    def reset(self):
        self.board = []
        self.cmap = {}
        self.fmap = {}

    def append(self, line):
        self.board.append(line.strip())

    # cindex: char index to find
    # point: current point
    def find_next(self, point, word, cindex): 
        fkey = self.mk_fmap_key(point, word, cindex)
        if fkey in self.fmap:
            return self.fmap[fkey]
        if cindex == len(word):
            return True

        x = int(point[0])
        y = int(point[1])
        c = word[cindex]

        next_points = []
        next_points.append( str(x-1) + str(y-1) )
        next_points.append( str(x-1) + str(y) )
        next_points.append( str(x-1) + str(y+1) )
        next_points.append( str(x) + str(y-1) )
        next_points.append( str(x) + str(y+1) )
        next_points.append( str(x+1) + str(y-1) )
        next_points.append( str(x+1) + str(y) )
        next_points.append( str(x+1) + str(y+1) )

        for np in next_points:
            if c == self.get(np):
                if self.find_next(np, word, cindex+1) == True:
                    return True

        self.fmap[fkey]=False
        return False
    def find(self, word):
        if word[0] not in self.cmap:
            return False
        for p in self.cmap[word[0]]:
            if self.find_next(p, word, 1) == True:
                return True
        return False

    def prepare(self):
        for i in range(5):
            for j in range(5):
                c = self.board[i][j]
                if c not in self.cmap:
                    self.cmap[c] = []
                self.cmap[c].append(str(i) + str(j))

    def get(self, index):
        if len(index) != 2:
            return ' '

        x = int(index[0])
        y = int(index[1])

        if x >= 5 or y >= 5:
            return ' '

        return self.board[x][y]


n_sets = int(rl())
b = Boggle()

for i in range(n_sets):
    b.reset()

    for j in range(5):
        b.append(rl())

    b.prepare()

    n_words = int(rl())
    for j in range(n_words):
        word = rl().strip()
        if b.find(word) == True:
            print word + " YES"
        else:
            print word + " NO"



