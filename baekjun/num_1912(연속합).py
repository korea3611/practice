n = int(input())
n_list = list(map(int,input().split()))
sum = [n_list[0]]
for i in range(len(n_list) - 1):
    sum.append(max(sum[i] + n_list[i+1], n_list[i+1]))
print(max(sum))
