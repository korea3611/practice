import sys
arr = []
dp = []
l = int(input())

for _ in range(l):
    arr.append(int(input()))

if l == 1:
    print(arr[0])
    sys.exit()
if l == 2:
    print(sum(arr))
    sys.exit()
if l == 3:
    print(max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2]))
    sys.exit()

dp.append(arr[0])
dp.append(arr[0]+arr[1])
dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
for i in range(3,l):
    dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i - 1]))

print(dp.pop())



