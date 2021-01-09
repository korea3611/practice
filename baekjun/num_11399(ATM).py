n = int(input())
arr = list(map(int,input().split()))
# print(arr)
arr.sort()
# print(arr)
sum1 = 0
a = []

for i in arr:
    sum1 += int(i)
    a.append(sum1)
print(sum(a))