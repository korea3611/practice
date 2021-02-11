## dfs 사용

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
# print(graph)

def dfs(x,y):
    global nums
    if x <= -1 or x>=n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        nums += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


nums = 0
numlist = []
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result += 1
            numlist.append(nums)
            nums = 0

print(result)
for i in sorted(numlist):
    print(i)