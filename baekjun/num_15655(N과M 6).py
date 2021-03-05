n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
c = [False]*(n+1)
a = [0]*m

def go(index, start, n ,m):
    if index == m:
        print(*a)
        return
    for i in data[start-1:]:
        if c[data.index(i)]:
            continue
        c[data.index(i)] = True
        a[index] = i
        go(index+1, data.index(i)+1, n, m)
        c[data.index(i)] = False

go(0,1,n,m)