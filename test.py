n, m = map(int,input().split())
dp = [0] * 31
dp[0] = 1
result = 1

for i in range(1,n+1):
    dp[i] = i*dp[i-1]
for _ in range(m):
    result *= n
    n -= 1

print(result//dp[m])

