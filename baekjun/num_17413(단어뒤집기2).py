s,tmp = input(), ""

ck = False

for i in s:
    if i == ' ':
        if not ck:
            print(tmp[::-1], end=" ")
            tmp = ""
        else:
            print(" ", end="")
    elif i == '<':
        ck = True
        print(tmp[::-1], end="")
        print("<", end="")
        tmp = ""
    elif i == '>':
        ck = False
        print(">", end="")
    else: # 알파벳과 숫자
        if ck:
            print(i, end="")
        else:
            tmp += i

print(tmp[::-1])