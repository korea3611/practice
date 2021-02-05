from collections import deque
n,m = map(int,input().split())
data = list(map(int,input().split()))
q = deque(i for i in range(1,n+1))
cnt = 0
sum = 0

for i in data:
    cnt = 0
    while True:
        if i == q[0]:
            sum += cnt
            q.popleft()
            break
        elif q.index(i) > len(q) // 2:
            cnt += 1
            x = q.pop()
            q.appendleft(x)
        else:
            cnt += 1
            x = q.popleft()
            q.append(x)

print(sum)





