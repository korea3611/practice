from collections import deque

m,n = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

dx,dy = [-1,1,0,0], [0,0,-1,1]
q = deque()

for i in range(n):
    for j in range(m):
        q.append((i,j))
        data[i][j] = 0


def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if  (0<=nx<n) and (0<=ny<m) and (data[nx][ny]) == 0:
                data[nx][ny] = data[x][y] + 1
                q.append((nx,ny))

    return data

print(bfs())