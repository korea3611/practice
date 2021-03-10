# from itertools import permutations
#
# n,m = map(int,input().split())
# data = [i for i in range(1,n+1)]
# data = list(permutations(data, m))
#
# for i in data:
#     for j in i:
#         print(j, end=' ')
#     print()

############

n,m = map(int,input().split())
c = [False]*(n+1)
a = [0]*m

def go(index, n, m):
    if index == m:
        print(*a)
        return
    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, n, m)
        c[i] = False

go(0,n,m)