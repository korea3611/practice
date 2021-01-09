##스택에 원소를 삽입할 때에는 단순히 특정 수에 도달할 수있는지 확인하면됨
##스택에서 원소를 빼낼 때에는 내림차순을 유지 할 수 있는지 확인하면됨

n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)  ##그냥 코드를 끝냄(아래의 print문 출력 안함)

print('\n'.join(result))




