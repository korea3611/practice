n = int(input())

a = [[0]*(n+1) for _ in range(n+1)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    data = list(map(int,input().split()))
    for j in range(len(data)):
        a[i][j+1] = data[j]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+a[i][j]

print(max(dp[-1]))