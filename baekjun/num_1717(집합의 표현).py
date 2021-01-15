import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for i in range(m):
    oper ,a ,b = map(int,input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES\n")
        else:
            print("NO\n")

##############################################################
# import sys
# input = sys.stdin.readline
#
# def get_parent(x):
#     if parent[x] == x:
#         return x
#     p = get_parent(parent[x])
#     parent[x] = p
#     return p
#
# def union(x, y):
#     x = get_parent(x)
#     y = get_parent(y)
#
#     if x != y:
#         parent[y] = x
#
# def find_parent(x):
#     if parent[x] == x:
#         return x
#     return find_parent(parent[x])
#
# n, m = map(int, input().split())
# parent = {}
#
# for i in range(n+1):
#     parent[i] = i
#
# for _ in range(m):
#     z, x, y = map(int, input().split())
#
#     if not z:
#         union(x, y)
#
#     if z:
#         if find_parent(x) == find_parent(y):
#             print('YES')
#         else:
#             print('NO')