# from collections import deque
#
# s = list(input())
# left = deque(s)
# right = deque()
# data = []
#
# n = int(input())
# for _ in range(n):
#     data.append(input().split())
#
# for i in data:
#     if len(i) >= 2 and i[0] == 'P':
#         left.append(i[1])
#     else:
#         if i[0] == 'L' and left:
#             a = left.pop()
#             right.appendleft(a)
#         elif i[0] == 'D' and right:
#             a = right.popleft()
#             left.append(a)
#         elif i[0] == 'B' and left:
#             a = left.pop()
#         else:
#             continue
#
# left.extend(right)
# print(''.join(left))
#
#

from sys import stdin

stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin:
    if line[0] == 'L':
        if stk1:
            stk2.append(stk1.pop())
        else:
            continue
    elif line[0] == 'D':
        if stk2:
            stk1.append(stk2.pop())
        else:
            continue
    elif line[0] == 'B':
        if stk1:
            stk1.pop()
        else:
            continue
    elif line[0] == 'P':
        stk1.append(line[2])
print(''.join(stk1 + list(reversed(stk2))))
