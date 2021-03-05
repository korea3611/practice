n = input()
n_len = len(n) - 1
c = 0
i = 0
while i < n_len:
    c += 9 * (10 ** i) * (i + 1)
    i += 1
c += ((int(n) - (10 ** n_len)) + 1) * (n_len + 1)
print(c)

##########

n = int(input())
ans = 0
start = 1
length = 1
while start <= n:
    end = start*10-1
    if end > n:
        end = n
    ans += (end-start+1)*length
    start *= 10
    length += 1
print(ans)