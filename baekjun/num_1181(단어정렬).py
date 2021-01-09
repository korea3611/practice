n = int(input())
arr = []
result = []
for i in range(n):
    arr.append(input())
arr.sort()
arr.sort(key=lambda x:(len(x)))

for i in arr:
    if i not in result:
        result.append(i)


print('\n'.join(result))