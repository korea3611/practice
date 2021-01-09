import sys
n = int(input())
k = int(input())
list = list(map(int, input().split()))
list = sorted(list)
arr = []

for i in range(len(list) - 1):
    arr.append(abs(list[i + 1] - list[i]))

arr = sorted(arr)
# print(arr)
# arr.remove(arr[-1])
# print(arr)
if n > k:
    for i in range(k - 1):
        arr.remove(arr[-1])
else:
    print(0)
    sys.exit()

print(sum(arr))
