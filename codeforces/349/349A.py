import sys


n = int(sys.stdin.readline().strip())

line = [i for i in sys.stdin.readline().strip().split(' ', n)]

stash = {'25': 0, '50': 0, '100': 0}

flag = True
for pay in line:
    if pay == '25':
        stash['25'] += 1
    elif pay == '50':
        stash['50'] += 1
        if stash['25'] == 0:
            flag = False
            break
        stash['25'] -= 1
    elif pay == '100':
        stash['100'] += 1
        if stash['50'] == 0:
            if stash['25'] < 3:
                flag = False
                break
            stash['25'] -= 3
        else:
            if stash['25'] == 0:
                flag = False
                break
            stash['50'] -= 1
            stash['25'] -= 1

if flag:
    print('YES')
else:
    print('NO')
