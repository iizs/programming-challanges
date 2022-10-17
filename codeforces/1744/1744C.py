import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    cs = sys.stdin.readline().strip().split()
    array_line = sys.stdin.readline().strip()

    c = int(cs[0])
    s = cs[1]
    if s == 'g':
        print('0')
        continue;

    lights = [e for e in array_line]
    lights.extend(lights[:c-1])

    max_y = 0
    max_r = 0
    int_y = -1
    int_r = -1
    for e in lights:
        if e == 'g':
            if int_y != -1:
                int_y += 1
                if int_y > max_y:
                    max_y = int_y
                int_y = -1
            if int_r != -1:
                int_r += 1
                if int_r > max_r:
                    max_r = int_r
                int_r = -1
        elif e == 'r':
            if int_y != -1:
                int_y += 1
            int_r += 1
        elif e == 'y':
            if int_r != -1:
                int_r += 1
            int_y += 1
    if s == 'r':
        print(max_r)
    elif s == 'y':
        print(max_y)



