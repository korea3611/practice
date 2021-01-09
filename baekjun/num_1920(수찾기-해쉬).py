a = int(input())
a_list = list(map(int, input().split()))
b = int(input())
b_list = list(map(int, input().split()))

for item in b_list:
    if item in a_list:
        print(1)
    else:
        print(0)