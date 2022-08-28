import sys
import queue


class Maze:
    def __init__(self, q):
        self.n = int(q[0])
        self.m = int(q[1])
        self.s_x = int(q[2])
        self.s_y = int(q[3])
        self.d = int(q[4])
        self.laser_blocks_up = False
        self.laser_blocks_down = False
        self.laser_blocks_left = False
        self.laser_blocks_right = False

        if self.s_x - self.d <= 1:
            self.laser_blocks_left = True
        if self.s_x + self.d >= self.n:
            self.laser_blocks_right = True
        if self.s_y - self.d <= 1:
            self.laser_blocks_up = True
        if self.s_y + self.d >= self.m:
            self.laser_blocks_down = True

    def x_y_to_idx(self, x, y):
        return (x - 1) + (y - 1) * self.n

    def get_num_of_moves_to_exit(self):

        if self.laser_blocks_right and self.laser_blocks_left:
            return -1
        if self.laser_blocks_up and self.laser_blocks_down:
            return -1
        if self.laser_blocks_down and self.laser_blocks_right:
            return -1
        if self.laser_blocks_up and self.laser_blocks_left:
            return -1

        return (self.m - 1) + (self.n - 1)


n = int(sys.stdin.readline().strip())

for i in range(n):
    q = sys.stdin.readline().strip().split()

    maze = Maze(q)
    print(maze.get_num_of_moves_to_exit())
