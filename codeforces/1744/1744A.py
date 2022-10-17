import sys

nq = int(sys.stdin.readline().strip())

for i in range(nq):
    n = int(sys.stdin.readline().strip())
    array_line = sys.stdin.readline().strip().split()
    word = sys.stdin.readline().strip()

    list_a = [int(e) for e in array_line]
    list_word = [c for c in word]
    # print(list_a)
    # print(list_word)

    if len(list_word) != len(list_a):
        print("NO")
        continue

    char_map = {}
    no_printed = False
    for j in range(len(list_word)):
        a = list_a[j]
        c = list_word[j]
        if a in char_map:
            if char_map[a] != c:
                print("NO")
                no_printed = True
                break
        else:
            char_map[a] = c
    if not no_printed:
        print("YES")

