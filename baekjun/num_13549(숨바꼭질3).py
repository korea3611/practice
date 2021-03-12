from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            return
        for i in (x-1, x+1, x*2):
            if 0<=i<100001 and dist[i] == 0:
                if i == x*2 and x != 0:
                    q.appendleft(i)
                    dist[i] = dist[x]
                else:
                    q.append(i)
                    dist[i] = dist[x]+1

n,k = map(int,input().split())
dist = [0]*100001
bfs()
