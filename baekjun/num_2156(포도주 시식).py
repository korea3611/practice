import sys
### n = 1 이라면 최대값은 첫번째
### n = 2 이라면 최대값은 첫번째 + 두번째
### n = 3 이라면 최대값은 첫번째 + 두번째 or 첫번째 + 세번째 or 두번째 + 세번째
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

if n == 1:
    print(data[0])
    sys.exit()
if n == 2:
    print(data[0] + data[1])
    sys.exit()
if n == 3:
    print(max(data[0]+data[1], data[0]+data[2], data[1]+data[2]))
    sys.exit()

dp = [0] * 10001
dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(data[0]+data[1], data[0]+data[2], data[1]+data[2])
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3] + data[i-1] + data[i],dp[i-2] + data[i] )


print(dp[n-1])