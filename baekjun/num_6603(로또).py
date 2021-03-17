def dfs(start, depth):
    if depth == 6:
        print(*a)
        return
    for i in range(start, len(data)):
        a[depth] = data[i]
        dfs(i+1, depth+1)

a = [0]*6
while True:
    data = list(map(int,input().split()))
    if data[0] == 0:
        break
    del data[0]
    dfs(0,0)
    print()