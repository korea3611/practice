import copy
# n : 전체학생의 수
# lost : 체육복을 도난당한 학생들의 번호가 담긴 배열
# reverse : 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
def solution(n, lost, reserve):
    copy_lost = copy.deepcopy(lost)
    copy_reserve = copy.deepcopy(reserve)
    for i in lost:
        if i in reserve:
            copy_lost.remove(i)
            copy_reserve.remove(i)

    print(copy_lost, copy_reserve)
    cnt = 0

    for i in copy_lost:
        if i-1 in copy_reserve:
            copy_reserve.remove(i-1)
            cnt += 1
        elif i+1 in copy_reserve:
            copy_reserve.remove(i+1)
            cnt += 1



    return n - len(copy_lost) + cnt


print(solution(5,[2,4],[1,3,5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [1, 2], [2, 3]))
print(solution(30, [1, 3], [2, 4, 5]))
print(solution(5, [1, 2, 4, 5], [2, 3, 4]))