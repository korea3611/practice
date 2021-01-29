import sys
from itertools import permutations
input = sys.stdin.readline

n = [1,2,3,4,5,6,7,8,9]
num = list(permutations(n,3))
t = int(input())

for _ in range(t):
    test, s,b = map(int, input().split())
    test = list(str(test))
    cnt = 0

    len_num = len(num)
    for i in range(len_num):
        s_cnt, b_cnt = 0,0
        i -= cnt

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            cnt += 1

print(len(num))



