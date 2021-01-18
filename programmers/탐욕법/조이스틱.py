def solution(name):
    answer = 0
    data = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    li = list(name)
    print(li)
    for i in li:
        if data.index(i) > 13:
            pass
        else:
            answer += data.index(i)
    print(answer)

solution("ABC")