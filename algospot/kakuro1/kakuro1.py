import sys
from operator import itemgetter, attrgetter

rl = lambda: sys.stdin.readline()

class Kakuro(object):
    def __init__(self):
        self.size = int(rl())
        self.answer = []
        self.prob_board = []
        self.prob_hint = []
        for i in range(self.size):
            l = [int(x) for x in rl().strip().split(' ')]
            self.answer.append(l)
            self.prob_board.append( [0 if x==0 else 1 for x in l] )
            p = None
            s = 0
            for j in range(len(l)):
                if p == None :
                    if l[j] > 0:
                        # Begin horizontal sum
                        p = (i+1,j)
                        s = l[j]
                    else:
                        pass
                else:
                    if l[j] > 0:
                        # continue horizontal sum
                        s += l[j]
                    else:
                        # end horizontal sum
                        self.prob_hint.append( [p[0], p[1], 0, s ])
                        p = None
            if p != None:
                # end horizontal sum
                self.prob_hint.append( [p[0], p[1], 0, s ])

        for j in range(self.size):
            p = None
            s = 0
            for i in range(self.size):
                if p == None :
                    if self.answer[i][j] > 0:
                        # Begin vertical sum
                        p = (i,j+1)
                        s = self.answer[i][j]
                    else:
                        pass
                else:
                    if self.answer[i][j] > 0:
                        # continue vertical sum
                        s += self.answer[i][j]
                    else:
                        # end vertical sum
                        self.prob_hint.append( [p[0], p[1], 1, s ])
                        p = None
            if p != None:
                # end vertical sum
                self.prob_hint.append( [p[0], p[1], 1, s ])
                
        self.prob_hint = sorted(self.prob_hint, key=itemgetter(2, 0, 1))

    def print_out(self):
        print self.size
        for i in range(len(self.prob_board)):
            print ' '.join(str(x) for x in self.prob_board[i] )
        print len(self.prob_hint)
        for i in range(len(self.prob_hint)):
            print ' '.join(str(x) for x in self.prob_hint[i] )



# main
n_sets = int(rl())

print n_sets
for i in range(n_sets):
    k = Kakuro()
    k.print_out()
