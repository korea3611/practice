from sys import stdin
k,n = map(int,stdin.readline().split())
data = [int(stdin.readline()) for _ in range(k)]
start, end = 1,sum(data)//n

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in data:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)