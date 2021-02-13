import sys
input = sys.stdin.readline

n,p = map(int,input().split())
datas = [list(map(int,input().split())) for _ in range(n)]
stack = [[] for _ in range(7)]
cnt = 0

for data in datas:
    if not stack[data[0]]:
        cnt += 1
        stack[data[0]].append(data[1])
        continue
    while stack[data[0]] and stack[data[0]][-1] > data[1]:
        stack[data[0]].pop()
        cnt += 1
    if stack[data[0]] and stack[data[0]][-1] == data[1]:
        continue
    else:
        stack[data[0]].append(data[1])
        cnt += 1

print(cnt)

