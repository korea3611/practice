## 하나의 문제를 제한 조건을 통해 쉬운 버전과 어려운 버전으로 나누어
## 쉬운 버전만 맞더라도 부분 점수를 주는 서브태스크 문제로 대회를 구성
## 입력
## N:문제의 개수 L:현정이의 역량 K:대회중에 풀 수 있는 문제의 최대개수

n,l,k = map(int,input().split())
arr = []
sum = 0
# print(arr)

for i in range(n):
    arr.append(list(map(int,input().split())))
# print(arr)

## i는 개별리스트
## j는 개별리스트의 항목
for i in arr:
    if max(i) <= l:
        sum += 140
    elif min(i) <= l:
        sum += 100
    else:
        continue

print(sum)
