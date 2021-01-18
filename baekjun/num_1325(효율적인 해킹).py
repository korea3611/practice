## 이건 왜 안되는지 모르겠지만 아래에 내가 쓴 정답코드가 있음
from collections import deque
n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    adj[y].append(x)
def bfs(v):
    q = deque([v])
    visited = [False] * (n+1)
    visited[v] = False
    count = 1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
    return count
result = []
max_value = -1
for i in range(1, n+1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
for e in result:
    print(e, end=" ")


######내가 쓴 정답코드!!

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