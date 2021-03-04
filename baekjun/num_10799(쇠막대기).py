s = input()
s = s.replace('()','a')
answer = 0
stack = []

for i in s:
    if i == '(':
        stack.append(i)
    elif i == 'a':
        answer += len(stack)
    else:
        stack.pop()
        answer += 1

print(answer)
