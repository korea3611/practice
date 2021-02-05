import sys
n ,m = map(int,input().split())
set1 = {input() for _ in range(n)}
set2 = {input() for _ in range(m)}
three = list(set1 & set2)

three = set(three)
print(len(three))
for i in sorted(three):
    print(i)