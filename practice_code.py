n = int(input())
n_list = [list(map(int,input().split())) for _ in range(n)]
a,b,c,d = 0,0,0,0
ck = [[0]*n for _ in range(n)]
while True:
    result = []
    a += 1
    result.append(a)
    for i in range(1,n):
        num = n_list[0][i] - a
        result.append(num)
    for i in range(n):
        for j in range(n):
            if i == j:
                ck[i][j] = 0
            else:
                ck[i][j] = result[i]+result[j]

    if ck == n_list:
        break

for i in range(len(result)):
    print(result[i], end=' ')
