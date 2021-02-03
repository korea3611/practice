## pypy3만 가능
## python3에서는 시간초과

n, k = map(int,input().split())
cnt = 0

for i in range(1, n+1):
    s = str(i)
    for j in range(len(s)):
        cnt += 1
        if cnt == k:
            print(s[j])
            exit(0)
print(-1)

