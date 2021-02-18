from collections import deque

n,t,g = map(int,input().split())
q = deque()
q.append(n)
cnt = 0

def check():
    global cnt
    while q:
        x = q.popleft()
        cnt += 1
        if x == g:
            return cnt
