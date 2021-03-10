data = [list(map(int,input())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            zero.append((i,j))

def garo(x, num):
    for i in range(0, 9):
        if data[x][i] == num:
            return False
    return True

def sero(y, num):
    for i in range(0, 9):
        if data[i][y] == num:
            return False
    return True

def square(x, y, num):
    moX = x // 3
    moY = y // 3
    for i in range(0, 3):
        for j in range(0, 3):
            if num == data[3*moX + i][3*moY + j]:
                return False
    return True

def backtracking(idx):
    if idx == len(zero):
        for i in data:
            for j in i:
                print(j, end='')
            print()
        return True
    x = zero[idx][0]
    y = zero[idx][1]
    for i in range(1, 10):
        if garo(x, i) == False:
            continue
        if sero(y, i) == False:
            continue
        if square(x, y, i) == False:
            continue
        data[x][y] = i
        res = backtracking(idx+1)
        if res == True:
            return True
        else:
            data[x][y] = 0
    return False

backtracking(0)