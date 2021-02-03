import heapq
n = int(input())
data = []
result = []
for _ in range(n):
    x,y = map(int,input().split())
    data.append([x,y])

data = sorted(data, key=lambda x:x[0])

for i in range(n):
    if len(result) != 0 and result[0] <= data[i][0]:
        print(result[0])
        heapq.heappop(result)
    heapq.heappush(result, data[i][1])

print(len(result))

