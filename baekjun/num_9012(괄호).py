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


