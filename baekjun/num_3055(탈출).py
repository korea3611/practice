from collections import deque
import sys
input = sys.stdin.readline

# 행과 열 입력받기
r, c = map(int,input().split())

# 물, 거리에 대한 deque
q = deque()
w = deque()
MAP = []
visit = [[0]*c for _ in range(r)]
dx, dy = [-1,1,0,0],[0,0,-1,1]

def bfs():
    while q or w:
        temp1 = []
        temp2 = []
        while q:
            x,y = q.popleft()
            if MAP[x][y] != '*':
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0<=nx<r and 0<=ny<c and visit[nx][ny]==0 and MAP[nx][ny]!='X' and MAP[nx][ny]!='*':
                        MAP[nx][ny] = MAP[x][y] + 1
                        visit[nx][ny] = 1
                        temp1.append((nx,ny))

        while w:
            x,y = w.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx == d[0] and ny == d[1]:
                    continue
                if 0<=nx<r and 0<=ny<c and MAP[nx][ny]!='*' and MAP[nx][ny] != 'X':
                    MAP[nx][ny] = '*'
                    temp2.append((nx,ny))

        for i in temp1:
            q.append(i)
        for i in temp2:
            w.append(i)


# 반복문으로 데이터 입력받기
for i in range(r):
    data = list(input())
    MAP.append(data)
    for j in range(c):
        if data[j] == 'S':
            q.append((i,j))
            visit[i][j] = 1
            MAP[i][j] = 0
        elif data[j] == '*':
            w.append((i,j))
        elif data[j] == 'D':
            d = [i,j]


bfs()
result = MAP[d[0]][d[1]]

print(result if result != "D" else "KAKTUS")

