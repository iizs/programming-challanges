import sys
import queue


class Maze:
    def __init__(self, q):
        self.n = int(q[0])
        self.m = int(q[1])
        self.s_x = int(q[2])
        self.s_y = int(q[3])
        self.d = int(q[4])
        self.maze = [99] * (self.m * self.n)
        self.laser_blocks_up = False
        self.laser_blocks_down = False
        self.laser_blocks_left = False
        self.laser_blocks_right = False
        self.q = queue.Queue()
        self.__set_laser__(self.s_x, self.s_y, 0)

    def x_y_to_idx(self, x, y):
        return (x - 1) + (y - 1) * self.n

    def __set_laser__(self, x, y, d):
        self.q.put((x, y, d))
        while not self.q.empty():
            item = self.q.get()
            self.__set_laser_inner__(item[0], item[1], item[2])

    def __set_laser_inner__(self, x, y, d):
        if x <= 0 or x > self.n:
            return
        if y <= 0 or y > self.m:
            return
        if self.maze[self.x_y_to_idx(x, y)] == -1:
            return

        self.maze[self.x_y_to_idx(x, y)] = -1

        if x == 1:
            self.laser_blocks_left = True
        if x == self.n:
            self.laser_blocks_right = True
        if y == 1:
            self.laser_blocks_up = True
        if y == self.m:
            self.laser_blocks_down = True

        if d == self.d:
            return
        d += 1
        self.q.put((x - 1, y, d))
        self.q.put((x + 1, y, d))
        self.q.put((x, y + 1, d))
        self.q.put((x, y - 1, d))

    def get_num_of_moves_to_exit(self):
        if self.maze[-1] == -1:
            return -1
        if self.laser_blocks_right and self.laser_blocks_left:
            return -1
        if self.laser_blocks_up and self.laser_blocks_down:
            return -1
        if self.laser_blocks_down and self.laser_blocks_right:
            return -1
        if self.laser_blocks_up and self.laser_blocks_left:
            return -1

        return (self.m - 1) + (self.n - 1)

    def print_maze(self):
        for i in range(self.m):
            print(self.maze[i*self.n:(i+1)*self.n])
        print('---')
        print(f'U blocked: {self.laser_blocks_up}')
        print(f'D blocked: {self.laser_blocks_down}')
        print(f'L blocked: {self.laser_blocks_left}')
        print(f'R blocked: {self.laser_blocks_right}')
        print('---')


n = int(sys.stdin.readline().strip())

for i in range(n):
    q = sys.stdin.readline().strip().split()

    maze = Maze(q)
    # maze.print_maze()
    print(maze.get_num_of_moves_to_exit())
    # maze.print_maze()
