from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())
data = [-1]*(f+1)
q = deque()
q.append(s)

def bfs():
    q = deque()
    q.append(s)
    data[s] = 0
    while q:
        now = q.popleft()
        if now == g:
            return data[now]
        for next in [now+u, now-d]:
            if 1 <= next < len(data) and data[next] == -1:
                data[next] = data[now] + 1
                q.append(next)
    return 'use the stairs'

print(bfs())
