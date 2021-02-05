s = list(input())
stack = []
ck = []
def check(s):
    for i in s:
        if i == ')':
            if ck:
                a = ck.pop()
                if a == '(':
                    pass
                else:
                    return False
            else:
                return False
        elif i ==']':
            if ck:
                a = ck.pop()
                if a == '[':
                    pass
                else:
                    return False
            else:
                return False
        else:
            ck.append(i)
    if ck:
        return False
    else:
        return True

if check(s):
    for i in s:
        if i == ')':
            k = 0
            while True:
                if stack:
                    a = stack.pop()
                    if a == '(':
                        if k == 0:
                            stack.append(2)
                        else:
                            stack.append(2 * k)
                        break
                    else:
                        k += a
                else:
                    break
        elif i == ']':
            k = 0
            while True:
                if stack:
                    a = stack.pop()
                    if a == '[':
                        if k == 0:
                            stack.append(3)
                        else:
                            stack.append(3 * k)
                        break
                    else:
                        k += a
                else:
                    break
        else:
            stack.append(i)
    print(sum(stack))

else:
    print(0)

