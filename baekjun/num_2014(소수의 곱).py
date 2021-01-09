import heapq
import copy

k,n = map(int,input().split())
p_list = list(map(int,input().split()))

lst, ck = copy.deepcopy(p_list), set()

heapq.heapify(lst)
ith = 0

while ith < n:
    mn = heapq.heappop(lst)
    if mn in ck:
        continue
    ith += 1
    ck.add(mn)
    for i in p_list:
        heapq.heappush(lst, mn*i)

print(mn)