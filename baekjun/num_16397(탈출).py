## 틀림 다시 제대로 풀어보자
from collections import deque

n,t,g = map(int,input().split())
data = [0]*100000
q = deque()
q.append(n)
data[7142] = 1
cnt = 0

def bfs():
    global cnt
    while q:
        cnt += 1
        now = q.popleft()
        if now == g:
            return data[now]
        for i in range(2):
            if i == 0:
                next = now+1
                if data[next] != 0:
                    if next > 99999:
                        continue
                    else:
                        data[next] = data[now] + 1
                        q.append(next)
                else:
                    continue
            elif i == 1:
                next = now * 2
                if data[next] != 0:
                    if next > 99999:
                        continue
                    else:
                        next_list = list(str(next))
                        next_list[0] = str(int(next_list[0])-1) if int(next_list[0])-1 > 0 else str(0)
                        next = int("".join(next_list))
                        data[next] = data[now] + 1
                        q.append(next)
                else:
                    continue
    return False

print(bfs())







