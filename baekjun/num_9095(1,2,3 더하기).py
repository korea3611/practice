n = int(input())
dp = [0]*12
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(n):
    num = int(input())
    print(dp[num])

################
def go(s, goal):
    if s > goal:
        return 0
    if s == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(s+i, goal)
    return now

t = int(input())
for _ in range(t):
    n = int(input())
    print(go(0,n))
