e,s,m = map(int,input().split())
x,y,z = 1,1,1
count = 1

while True:
    if x > 15:
        x = 1
    if y > 28:
        y = 1
    if z > 19:
        z = 1
    if x == e and y == s and z == m:
        break
    x += 1
    y += 1
    z += 1
    count += 1

print(count)