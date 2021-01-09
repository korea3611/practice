## 0 입력으로 팀에 속한 멤버의 이름 출력
## 1 입력으로 해당멤버가 속한 팀의 이름 출력
def check(girl_group_list, name, zero_one):
    if zero_one == 0:
        for girl_group in girl_group_list:
            for girl in girl_group:
                if girl == name:
                    # del girl_group[0]
                    girl_group2 = []
                    for i in range(1,len(girl_group)):
                        girl_group2.append(girl_group[i])
                    girl_group2.sort()
                    for i in girl_group2:
                        print(i)
    else:
        for girl_group in girl_group_list:
            for girl in girl_group:
                if girl == name:
                    print(girl_group[0])


## n은 총 입력받을 걸그룹의 수
## m은 맞혀야할 문제의 수
n, m = map(int, input().split())
girl_group_list = [[] for i in range(n)]
# print(girl_group_list)

for i in range(n):
    girl_group_list[i].append(input())
    num = int(input())
    for j in range(num):
        girl_group_list[i].append(input())

# print(girl_group_list)

for i in range(m):
    name = input()
    zero_one = int(input())
    check(girl_group_list, name, zero_one)
