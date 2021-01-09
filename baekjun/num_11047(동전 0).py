n, money = map(int,input().split())
arr = []
min_n = 0
for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse = True)

for i in arr:
    if i>money:
        continue
    else:
        min_n += (money // i)
        money -= i*(money//i)
        if money == 0:
            break

print(min_n)
