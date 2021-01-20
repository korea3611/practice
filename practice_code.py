n = int(input())

def mountain(n):
    if n == 1:
        print(1,end='')
    else:
        mountain(n-1)
        print(n,end='')
        mountain(n-1)

mountain(n)



