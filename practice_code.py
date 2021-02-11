n = int(input())
data = [list(map(int,input())) for _ in range(n)]

def dfs(x,y):
    global nums
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if data[x][y] == 1:
        nums += 1
        data[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

x = 0
nums = 0
result = []

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result.append(nums)
            nums = 0
            x += 1

print(x)
for i in sorted(result):
    print(i)