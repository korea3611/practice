import sys
n = int(input())

for i in range(n):
    s = input()
    left = 0
    right = 0
    if s[0] == ')':
        print('NO')
        continue
    if s.count('(') != s.count(')'):
        print("NO")
        continue
    else:
        for j in s:
            if j == '(':
                left += 1
            else:
                right += 1
            if right > left:
                print('NO')
                break

#### 내코드

n = int(input())

def check(data):
    if data.count('(') == data.count(')'):
        for i in data:
            if i == ')':
                if stack:
                    a = stack.pop()
                    if a == '(':
                        pass
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        return True
    else:
        return False


for _ in range(n):
    data = list(input())
    stack = []
    if check(data):
        print("YES")
    else:
        print("NO")


