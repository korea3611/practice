from itertools import permutations
import copy

n = [1,2,3,4,5,6,7,8,9]
n = list(permutations(n,3))
n_list = copy.deepcopy(n)
print(n)

#횟수 입력받기
t = int(input())
for _ in range(t):
    test, s, b = map(int,input().split())
    test = list(str(test))

    for i in n_list:
        cnt_s, cnt_b = 0,0
        for j in range(3):
            if int(test[j]) in i:
                print(test.index(test[j], i.index(int(test[j]))))
                if test.index(test[j]) == i.index(int(test[j])):
                    cnt_s += 1
                else:
                    cnt_b += 1

        if s != cnt_s or b != cnt_b:
            n.remove(i)

print(n)
