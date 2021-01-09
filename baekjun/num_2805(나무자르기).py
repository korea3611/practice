## 시간초과
from sys import stdin
n,m = map(int,stdin.readline().split())
data = list(map(int,stdin.readline().split()))

start = 0
end = max(data)

result = 0
while (start <= end):
    total = 0
    mid = (start+end) // 2
    for x in data:
        if x > mid:
            total += x-mid

    if total < m:
        end = m-1
    else:
        result = mid
        start = mid + 1

print(result)

##시간초과 안나는 코드
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2

    log = 0  # 벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid

    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)