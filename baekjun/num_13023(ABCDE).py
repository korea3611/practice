n,m = map(int,input().split())
adj = [[] for _ in range(n)]
visited = [False]*n
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(v, depth):
    global ans
    visited[v] = True
    if depth >= 4:
        ans = True
        return
    for nx in adj[v]:
        if not visited[nx]:
            dfs(nx, depth+1)
            visited[nx] = False

ans = False
for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break
print(1 if ans else 0)
