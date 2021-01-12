n = int(input())
result = []

while True:
    if n == 1:
        break
    for i in range(2, n+1):
        if n % i == 0:
            result.append(i)
            n //= i
            break
        else:
            continue

for i in result:
    print(i)
