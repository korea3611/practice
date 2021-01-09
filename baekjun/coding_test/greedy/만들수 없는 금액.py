n = int(input())
n_list = list(map(int,input().split()))
ans = 0
n_list.sort()

for i in n_list:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans+1)