from _collections import deque

n,m = map(int,input().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    data[b].append(a)

# print(data)

def bfs(start):
    global num
    q = deque([start])
    while q:
        v = q.popleft()
        if not visited[v]:
            num += 1
            visited[v] = True
            for e in data[v]:
                q.append(e)

num = 0
li = []
for i in range(n+1):
    visited = [False] * (n+1)
    bfs(i)
    li.append(num)
    num = 0

a = max(li)

for i in range(len(li)):
    if li[i] == a:
        print(i, end=' ')