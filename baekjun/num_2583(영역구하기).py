import sys
sys.setrecursionlimit(10000)

m,n,k = map(int,input().split())
data = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1, y2):
        for j in range(x1,x2):
            data[i][j] = 1


def dfs(x,y):
    global nums
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if data[x][y] == 0:
        nums += 1
        data[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False

nums = 0
result = []
cnt = 0

for i in range(m):
    for j in range(n):
        if dfs(i,j) == True:
            cnt += 1
            result.append(nums)
            nums = 0

print(cnt)
for i in sorted(result):
    print(i, end=' ')

