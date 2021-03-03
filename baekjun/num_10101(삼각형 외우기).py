data = [int(input()) for _ in range(3)]

if sum(data) != 180:
    print('Error')
elif len(set(data)) == 1:
    print('Equilateral')
elif len(set(data)) == 2:
    print('Isosceles')
else:
    print('Scalene')