import sys

def ck(i):
    num = list(str(i))
    for j in num:
        if j in del_list:
            return False
    return True

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
del_list = list(sys.stdin.readline().split())

result = abs(n - 100)

for i in range(1000001):
    if ck(i):
        result = min(result, len(str(i)) + abs(i-n))
print(result)

