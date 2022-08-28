import sys
import queue


class Maze:
    def __init__(self, q):
        self.n = int(q[0])
        self.m = int(q[1])
        self.s_x = int(q[2])
        self.s_y = int(q[3])
        self.d = int(q[4])
        self.maze = [self.m * self.n] * (self.m * self.n)
        self.__set_laser__(self.s_x, self.s_y, 0)
        self.q = queue.Queue()

    def x_y_to_idx(self, x, y):
        return (x - 1) + (y - 1) * self.n

    def __set_laser__(self, x, y, d):
        if x <= 0 or x > self.n:
            return
        if y <= 0 or y > self.m:
            return
        if self.maze[self.x_y_to_idx(x, y)] == -1:
            return

        self.maze[self.x_y_to_idx(x, y)] = -1
        if d == self.d:
            return
        d += 1
        self.__set_laser__(x - 1, y, d)
        self.__set_laser__(x + 1, y, d)
        self.__set_laser__(x, y + 1, d)
        self.__set_laser__(x, y - 1, d)

    def __set_distance__(self, x, y, d):
        self.q.put((x, y, d))
        while not self.q.empty():
            item = self.q.get()
            self.__set_distance_inner__(item[0], item[1], item[2])

    def __set_distance_inner__(self, x, y, d):
        if x <= 0 or x > self.n:
            return
        if y <= 0 or y > self.m:
            return
        if self.maze[self.x_y_to_idx(x, y)] <= d:
            return

        self.maze[self.x_y_to_idx(x, y)] = d

        d += 1
        self.q.put((x - 1, y, d))
        self.q.put((x + 1, y, d))
        self.q.put((x, y + 1, d))
        self.q.put((x, y - 1, d))

    def get_num_of_moves_to_exit(self):
        if self.maze[-1] == -1:
            return -1
        self.__set_distance__(1, 1, 1)

        if self.maze[-1] == self.m * self.n:
            return -1
        return self.maze[-1] - 1

    def print_maze(self):
        for i in range(self.m):
            print(self.maze[i*self.n:(i+1)*self.n])
        print('---')


n = int(sys.stdin.readline().strip())

for i in range(n):
    q = sys.stdin.readline().strip().split()

    maze = Maze(q)
    #maze.print_maze()
    print(maze.get_num_of_moves_to_exit())
    #maze.print_maze()


