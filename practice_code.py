from collections import deque
def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    arr.reverse()
    print(*arr)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            path(x)
            return
        for i in (x-1,x+1,x*2):
            if 0<=i<100001 and dist[i] == 0:
                dist[i] = dist[x]+1
                q.append(i)
                move[i] = x

n,k = map(int,input().split())
dist = [0]*100001
move = [0]*100001
bfs()
