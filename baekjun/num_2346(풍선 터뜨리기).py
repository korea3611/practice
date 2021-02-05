from collections import deque
n = int(input())
data = {}
result = []
start = 0
arr = list(map(int,input().split()))
for i in range(1,n+1):
    data[i] = arr[i-1]

q = deque([i for i in range(1,n+1)])

for i in data:
    if q[0] == 1:
        a = q.popleft()
        start += data[a]
        result.append(a)
    elif q and start > 0:
        for _ in range(start):
            a = q.popleft()
            q.append(a)
        a = q.pop()
        result.append(a)
        start = data[a]
    elif q and start < 0:
        for _ in range(-start):
            a = q.pop()
            q.appendleft(a)
        a = q.popleft()
        result.append(a)
        start = data[a]
    elif i == 1:
        a = q.popleft()
        result.append(a)

for i in result:
    print(i,end=' ')
