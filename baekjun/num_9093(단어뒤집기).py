n = int(input())
for _ in range(n):
    s = list(input().split())
    for i in s:

        a = list(i)
        a.reverse()
        for j in a:
            print(j, end='')
        print(end=' ')