A,B,V = map(int, input().split())

day = 1
dis = 0

if A >= V:
    print(1)
else:
    while True:
        dis += A
        if dis >= V:
            print(day)
            break
        dis -= B
        day += 1


########시간초과 코드 #######

a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)