from collections import deque

def bfs():
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == -1:
                    if a[nx][ny] == 0:
                        q.appendleft((nx,ny))
                        arr[nx][ny] = arr[x][y]
                    else:
                        q.append((nx,ny))
                        arr[nx][ny] = arr[x][y]+1

    return arr[n-1][m-1]


m,n = map(int,input().split())
arr = [[-1]*m for _ in range(n)]
arr[0][0] = 0
dx ,dy = [-1,1,0,0], [0,0,-1,1]
a = []
for i in range(n):
    a.append(list(map(int,input())))
print(bfs())




