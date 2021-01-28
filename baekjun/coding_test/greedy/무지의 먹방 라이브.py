n = int(input())

for _ in range(n):
    v = int(input())
    data = list(map(int,input().split()))
    data.sort()
    result = 0
    for i in range(2,v):
        c = data[i] - data[i-2]





