n = int(input())
list = list(input())
sum = 0
count = 0

for i in range(n):
    if list[i] == 'O':
        sum += i+1
        sum += count
        count += 1
    else:
        count = 0

print(sum)


