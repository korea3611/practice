## unionfind 사용

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent,a,b)

for i in range(1, v+1):
    find_parent(parent, i)

parent.remove(0)

print(len(set(parent)))

## bfs사용
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0]*(n+1)

def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

answer = 0
for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        answer += 1

print(answer)
