n = int(input())
data = list(input().split())
result = []

def ck(x, str):
    if str(x) in str:
        return False
    return True

def good(x,y,op):
    if op == '<':
        if x>y:
            return False
    if op == '>':
        if x<y:
            return False
    return True

def go(idx, str):
    if idx == n+1:
        result.append(str)
        return True
    for i in range(0,10):
        if ck(i, str) == False:
            continue
        if idx == 0 or good(str[i-1], str[i], data[idx]):
            go(idx+1, str+str[i])
    return False

go(0, '')
print(result)

