## 입력 첫째줄 화단의 한변의 길
## 이후 n개의 줄에 n개씩 화단의 지점당 가격이 주어짐
## 전수조사 + 방향벡터

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
## g = [[1, 0, 2, 3, 3, 4], [1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [3, 9, 9, 0, 1, 99], [9, 11, 3, 1, 0, 3], [12, 3, 0, 0, 0, 1]]
dx, dy = [0,0,0,1,-1], [0,1,-1,0,0]

ans = 10000

def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower//n
        y = flower%n
        if x == 0 or x == n-1 or y == 0 or y == n-1:
            return 10000
        for w in range(5):
            flow.append((x+dx[w], y+dy[w]))
            ret += g[x+dx[w]][y+dy[w]]
    if len(set(flow)) != 15:
        return 10000
    return ret


for i in range(n*n):
    for j in range(n*n):
        for k in range(n*n):
            ans = min(ans, ck([i,j,k]))

print(ans)


