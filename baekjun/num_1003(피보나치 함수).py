t = int(input())
data = [int(input()) for _ in range(t)]

d_zero = [0] * 41
d_one = [0] * 41
d_zero[0], d_zero[1] = 1,0
d_one[0], d_one[1] = 0,1

for i in data:
    if i == 0:
        print(d_zero[0], d_one[0])
    elif i == 1:
        print(d_zero[1], d_one[1])
    else:
        for j in range(2,i+1):
            d_zero[j] = d_zero[j-1] + d_zero[j-2]
            d_one[j] = d_one[j-1] + d_one[j-2]
        print(d_zero[i], d_one[i])

