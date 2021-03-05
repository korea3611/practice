from itertools import combinations

n,m = map(int,input().split())
data = [i for i in range(1,n+1)]
data = list(combinations(data, m))

for i in data:
    for j in i:
        print(j, end=' ')
    print()

#####################
n,m = map(int,input().split())
c = [False]*(n+1)
a = [0]*m

def go(index, start, n ,m):
    if index == m:
        print(' '.join(map(str, a)) + '\n')
        return
    for i in range(start, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, i+1, n, m)
        c[i] = False

go(0,1,n,m)