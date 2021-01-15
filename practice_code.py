n = int(input())
li = []
li2 = []
dp = [0 for i in range(n)]
for i in range(n):
    x,y = map(int,input().split())
    li.append((x,y))
li.sort()

for i in range(len(li)):
    li2.append(li[i][1])

print(li2)
dp[0] = 1

for i in range(1,n):
    a = 1
    for j in range(i):
        if li2[i] > li2[j]:
            a = max(a, dp[j] + 1)
    dp[i] = max(a, dp[i])

print(n - max(dp))
print(dp)



