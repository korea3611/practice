##N은 행렬의 크기, r은 행, c는 열
##모르겠다..

def solve(n,x,y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    solve(n/2,x,y)
    solve(n/2,x, y+n/2)
    solve(n/2, x+n/2,y)
    solve(n/2, x+n/2, y+n/2)

result = 0
N, X, Y = map(int,input().split())
solve(2**N,0,0)

###두번째코드

N,r,c = map(int,input().split())

def Z(sz,x,y):
    if sz == 1:
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if x < sz * (i+1) and y < sz * (j+1):
                return (i*2+j) * sz*sz + Z(sz, x-sz*i, y-sz*j)

print(Z(2**N,r,c))
