from itertools import permutations

n,m = map(int,input().split())
data = [i for i in range(1,n+1)]
data = list(permutations(data, m))

for i in data:
    for j in i:
        print(j, end=' ')
    print()