n = int(input())
sum = 0
count = 1

while n:
    if n < count:
        count = 1
    n -= count
    sum += 1
    count += 1

print(sum)
