n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

dp[0][0] = data[0][0]
steps = [[0,1], [1,0], [1,1]]

for x in range(n):
    for y in range(m):
        for step in steps:
            nx = x+step[0]
            ny = y+step[1]
            if 0<=nx<n and 0<=ny<m:
                dp[nx][ny] = max(dp[nx][ny],dp[x][y] + data[nx][ny])
print(dp[-1][-1])
