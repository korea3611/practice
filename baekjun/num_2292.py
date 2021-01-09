num = int(input())

first = 1
plus = 6
room = 1
if num == 1:
    print(1)
else:
    while True:
        first += plus
        room += 1
        if num <= first:
            print(room)
            break
        plus += 6



