n = int(input())
li = []
for i in range(n):
    a = list(map(int,input().split()))
    li.append(a)

cnt = 0

for i in li:
    int_sum = 0
    cnt = 0
    for y in i:
        if y == i[0]:
            continue
        elif y > float((sum(i)-i[0])/i[0]):
            cnt += 1

    print(str('%.3f' %float(cnt/i[0]*100)) + "%" )