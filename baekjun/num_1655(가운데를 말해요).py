## 이진탐색으로 구현한 코드
from bisect import bisect_left

n = int(input())
array = []

num = int(input())
array.append(num)

length = 1

for _ in range(n-1):
    num = int(input())
    index = bisect_left(array, num)
    array.insert(index, num)
    length += 1

    if length % 2 == 0:
        print(min(array[length // 2 - 1], array[length // 2]))
    else:
        print(array[length // 2])

## 우선순위 큐를 이용한 코드

import heapq
import sys

n = int(sys.stdin.readline())
max_heap = []
min_heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if min_heap and -max_heap[0] > min_heap[0]:
        a = heapq.heappop(min_heap)
        b = -heapq.heappop(max_heap)
        heapq.heappush(max_heap, -a)
        heapq.heappush(min_heap, b)

    print(-max_heap[0])






