n = int(input())
max_h = 1
max_l = 0
data = []
for i in range(n):
    l,h = map(int,input().split())
    data.append([l,h])
    if max_l < l:
        max_l = l
    if max_h < h:
        max_h = h
        maxIndex = l

h_list = [0] * (max_l + 1)
for l, h in data:
    h_list[l] = h

sum = 0
temp = 0
for i in range(maxIndex + 1):
    if h_list[i] > temp:
        temp = h_list[i]
    sum += temp
temp = 0
for i in range(max_l, maxIndex, -1):
    if h_list[i] > temp:
        temp = h_list[i]
    sum += temp

print(sum)