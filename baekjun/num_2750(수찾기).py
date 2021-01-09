a = int(input())
list = []

for i in range(a):
    list.append(int(input()))

list.sort()

for i in list:
    print(i)