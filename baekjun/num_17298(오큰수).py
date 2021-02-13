n = int(input())
data = list(map(int,input().split()))
stack = []
res = [-1] * n

for i in range(n):
    while stack and data[stack[-1]] < data[i]:
        res[stack[-1]] = data[i]
        stack.pop()
    stack.append(i)

for i in res:
    print(i, end=' ')
