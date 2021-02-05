n = input()
x = len(n) // 2

left = []
right = []

for i in range(x):
    left.append(int(n[i]))

for i in range(len(n)-1, x-1, -1):
    right.append(int(n[i]))

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")