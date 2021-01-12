x,y = map(int,input().split())
dis = y-x
count = 0
move = 1
moved = 0
while moved < dis:
    count += 1
    moved += move
    if count % 2 == 0:
        move += 1
print(count)

