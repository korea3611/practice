n = int(input())

li = []

for i in range(n):
    li.append(input())

for i in li:
    cnt = 0
    c = 1
    for y in i:
        if y == "o":
            cnt += c
            c += 1
        else:
            c = 1

    print(cnt)