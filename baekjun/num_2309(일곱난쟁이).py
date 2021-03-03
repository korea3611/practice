from itertools import combinations
data = [int(input()) for _ in range(9)]

data = list(combinations(data,7))

for i in data:
    if sum(i) == 100:
        a = list(i)
        break

a.sort()

for i in a:
    print(i)