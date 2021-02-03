n = int(input())
t = []
p = []
dp = [0]*(n+1)
print(dp)
for _ in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i + t[i]])

print(max(dp))
print(dp)