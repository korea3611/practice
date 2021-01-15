import itertools

def baseball_fun(x,y):
    x = list(x); y = list(y)
    s = 0; b = 0
    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i:
                s += 1
            else:
                b += 1
    return [s,b]

def solution(baseball_list):
    v = list(map(lambda x:str(x[0]), baseball_list))
    r = list(map(lambda x: [x[1], x[2]], baseball_list))

    all = list(itertools.permutations(range(1,10), 3))
    all = list(map(lambda x: list(map(str, x)), all))

    cnt = 0
    for x in all:
        if [baseball_fun(x,y) for y in v] == r:
            cnt += 1

    print(cnt)

n = int(input())
baseball_list = []
for i in range(n):
    a,b,c = map(int,input().split())
    baseball_list.append([a,b,c])

solution(baseball_list)