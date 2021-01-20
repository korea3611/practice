## answers = [1,2,3,4,5]
## 감격스럽다..
def solution(answers):
    answer = []
    result = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            cnt += 1
    answer.append(cnt)
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == two[i%8]:
            cnt += 1
    answer.append(cnt)
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == three[i%10]:
            cnt += 1
    answer.append(cnt)

    max_num = max(answer)

    for i,j in enumerate(answer):
        if j == max_num:
            result.append(i+1)

    return result



answers = [1,2,3,4,5]
solution(answers)
answers = [1,3,2,4,2]
solution(answers)
