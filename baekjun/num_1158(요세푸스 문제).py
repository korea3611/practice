n,k = map(int,input().split())
data = [i for i in range(1,n+1)]

result = []

i = k-1

while True:
    result.append(data.pop(i))
    if not data:
        break
    i = (i+k-1) % len(data)
print('<'+', '.join(map(str, result))+'>')




