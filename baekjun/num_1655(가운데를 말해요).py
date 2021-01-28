import heapq
n = int(input())
left, right = [], []

for _ in range(n):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))





