from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

def bfs():
    while q or f:
        temp1 = []
        temp2 = []
        while q:
            x, y = q.popleft()
            if s[x][y] != '#' and s[x][y] != '*':
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 and s[nx][ny] != '*' and s[nx][ny] != '#':
                        s[nx][ny] = s[x][y] + 1
                        visit[nx][ny] = 1
                        temp1.append((nx, ny))
                    elif 0 > nx or nx >= h or 0 > ny or ny >= w:
                        return s[x][y]

        while f:
            x, y = f.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != '*' and s[nx][ny] != '#':
                    s[nx][ny] = '*'
                    temp2.append((nx, ny))

        for i in temp1:
            q.append(i)
        for i in temp2:
            f.append(i)

    return "IMPOSSIBLE"

for i in range(n):
    w, h = map(int,input().split())
    s = []
    visit = [[0]*w for _ in range(h)]
    q = deque()
    f = deque()
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    for i in range(h):
        data = list(input())
        s.append(data)
        for j in range(w):
            if data[j] == '@':
                q.append((i,j))
                visit[i][j] = 1
                s[i][j] = 1
            elif data[j] == '*':
                f.append((i,j))


    print(bfs())

