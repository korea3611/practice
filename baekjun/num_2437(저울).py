n = int(input())
a = list(map(int,input().split()))
ans = 0
a.sort()
for i in a:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans + 1)