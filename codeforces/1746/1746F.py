import sys

nq = sys.stdin.readline().strip()
n = int(nq.split()[0])
q = int(nq.split()[1])

list_a_line = sys.stdin.readline().strip().split()
list_a = [int(e) for e in list_a_line]

# print(list_a)
for i in range(q):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == '1':
        list_a[int(cmd[1]) - 1] = int(cmd[2])
        # print(list_a)
    elif cmd[0] == '2':
        #sublist_a = list_a[int(cmd[1]) - 1:int(cmd[2])]
        # print(sublist_a)
        count_map = {}
        for i in range(int(cmd[1]) - 1, int(cmd[2])):
            e = list_a[i]
            if e not in count_map:
                count_map[e] = 0
            count_map[e] += 1
        k = int(cmd[3])
        divisible = True
        for key in count_map:
            if count_map[key] % k != 0:
                print('NO')
                divisible = False
                break
        if divisible:
            print('YES')
