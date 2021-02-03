s = list(input())
stack = []

def check(s):
    for i in s:
        if i == ')':
            a = stack.pop()
            if a == '(':
                pass
            else:
                return False
        elif i == ']':
            a = stack.pop()
            if a == '[':
                pass
            else:
                return False
        else:
            stack.append(i)
    return True

def solution(s):
    for i in s:
        pass

if check(s):
    print('dd')
else:
    print(0)