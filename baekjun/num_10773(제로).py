from collections import deque

n = int(input())
q = deque()
for i in range(n):
    x = int(input())
    if x == 0:
        q.pop()
    else:
        q.append(x)

print(sum(q))

