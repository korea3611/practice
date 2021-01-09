t = int(input())
arr = [int(input()) for _ in range(t)]

ck = [0] * 101
ck[1],ck[2],ck[3],ck[4],ck[5] = 1,1,1,2,2

for i in arr:
    if i <= 5:
        print(ck[i])
    else:
        for j in range(6, i+1):
            ck[j] = ck[j-1] + ck[j-5]
        print(ck[i])