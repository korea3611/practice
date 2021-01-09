## 내코드

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort(reverse=True)
count = 0
num = len(n_list)



while True:
    if len(n_list) == 0:
        break
    if num >= max(n_list):
        count += 1
        num -= max(n_list)
        for _ in range(max(n_list)):
            del n_list[0]
    else:
        break

print(count)

##############################

n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도가 낮은 것부터 하나씩 확인하며
    count += 1 #해당그룹에 해당 모험가 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0

print(result)