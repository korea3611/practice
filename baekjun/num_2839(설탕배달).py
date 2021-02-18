num = int(input())

box = 0

while True:
    if num%5 == 0:
        box += num//5
        print(box)
        break
    num -= 3
    box += 1
    if num < 0:
        print(-1)
        break

