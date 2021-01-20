from itertools import permutations

s = input()
result = []
result2 = []
for i in range(1,len(s)+1):
    a = permutations(s, i)
    a = list(a)
    result.append(a)

print(result)

for i in result:
    for j in i:
        x = ''
        for e in j:
            # print(e)
            x += e
            print(x)
        result2.append(x)

print(result2)

for i in result2:
    if int(i) == 1:
        result2.remove(i)
    else:
        for j in range(2,int(i)):
            if int(i) % j == 0:
                result2.remove(i)

print(result2)







# s = ('1','7')
# ans = ''
# for i in s:
#     ans += i
# print(ans)