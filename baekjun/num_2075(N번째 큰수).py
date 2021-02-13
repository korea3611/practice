import heapq
n = int(input())
heap = []

for _ in range(n):
    data = list(map(int,input().split()))
    for i in data:
        heapq.heappush(heap, i)
    while len(heap) > n:
        heapq.heappop(heap)

print(heapq.heappop(heap))