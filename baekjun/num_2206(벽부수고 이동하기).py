from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

# # print(graph)
# print(one_list)

dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][n-1]

print(bfs(0,0))