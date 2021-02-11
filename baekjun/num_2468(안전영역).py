import copy
import sys
sys.setrecursionlimit(10000)

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

max_num = 0
for i in range(n):
    for j in range(n):
        max_num = max(max_num, data[i][j])

# max_num 은 9가 됨
result = []
a = 0

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if data1[x][y] == 1:
        data1[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

cnt = 0
while a != max_num:
    cnt = 0
    data1 = copy.deepcopy(data)

    for i in range(n):
        for j in range(n):
            if data1[i][j] <= a:
                data1[i][j] = 0
            else:
                data1[i][j] = 1

    for i in range(n):
        for j in range(n):
            if dfs(i,j) == True:
                cnt += 1

    result.append(cnt)
    a += 1

print(max(result))


