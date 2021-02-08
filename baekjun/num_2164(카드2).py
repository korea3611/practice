from collections import deque
n = int(input())
q = deque([i for i in range(n, 0, -1)])

cnt = 1

while len(q) != 1:
    if cnt % 2 == 1:
        q.pop()
        cnt += 1
    else:
        a = q.pop()
        q.appendleft(a)
        cnt += 1

print(q[0])