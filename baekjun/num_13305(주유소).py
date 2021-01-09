n = int(input())
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

result = roads[0] * costs[0]
m = costs[0]
dist = 0

for i in range(1,n-1):
    if costs[i] < m:
        result += m*dist
        dist = roads[i]
        m = costs[i]
    else:
        dist += roads[i]

    if i == n-2:
        result += m*dist

print(result)

####다른 코드
n = int(input())
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))
res = 0
m = costs[0]
for i in range(n-1):
    if costs[i] < m:
        m = costs[i]
    res += m * roads[i]

print(res)