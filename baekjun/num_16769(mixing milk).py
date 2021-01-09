## C는 용량 리스트, M은 담겨있는 양 리스트
C, M = list(), list()

for i in range(3):
    a,b = map(int,input().split())
    C.append(a)
    M.append(b)

## 현재 담겨있는 것은 C = [10,11,12], M = [3,4,5]

for i in range(100):
    idx = i%3
    nxt = (idx+1) % 3

    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]),
                         0),min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)