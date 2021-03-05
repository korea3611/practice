n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
c = [False]*n
a = [0]*m

def go(index, n, m):
    if index == m:
        print(*a)
        return
    for i in data:
        c[data.index(i)] = True
        a[index] = i
        go(index+1, n,m)
        c[data.index(i)] = False

go(0,n,m)
