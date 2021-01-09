n = int(input())
arr = list(map(int, input().split()))
n_list = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            n_list[i] = max(n_list[i], n_list[j]+1)

print(max(n_list))



