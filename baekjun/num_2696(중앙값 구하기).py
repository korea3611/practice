import heapq
n = int(input())

for _ in range(n):
    data = list(map(int,input().split()))
    max_heap = []
    min_heap = []
    for i in data:
        if len(min_heap) == len(max_heap):
            heapq.heappush(min_heap, i)
        else:
            heapq.heappush(max_heap, -i)


        if -max_heap[0] < min_heap[0]:
            a = -heapq.heappop(max_heap)
            b = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -b)
            heapq.heappush(min_heap, a)
        if len(max_heap) + len(min_heap) % 2 == 1:
            print(min_heap[0])

