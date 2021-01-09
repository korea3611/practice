n,m = map(int,input().split())
data = []
for i in range(n):
    data.append(min(map(int,input().split())))

print(max(data))