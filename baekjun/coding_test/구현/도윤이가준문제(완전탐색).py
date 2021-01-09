import math
# 맵의 크기 입력받기
n = int(input())
# x좌표 y좌표 유닛의 사거리 입력받기
x, y, r = map(int, input().split())
# map 초기화
m = [[0] * n for _ in range(n)]
# print(m)
m[x - 1][y - 1] = 'x'
# print(m)
dx, dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]

# 1부터 r까지의 거리 넣어서 반복
for i in range(1, r + 1):
    for j in range(len(dx)):
            nx = x - 1 + dx[j]
            ny = y - 1 + dy[j]
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            else:
                if m[nx][ny] == 0:
                    m[nx][ny] = math.ceil(math.sqrt((nx-x)**2+(ny-y)**2))


for i in m:
    print(i)

