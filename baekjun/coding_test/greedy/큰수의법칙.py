# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰수를 만드는 방법
# 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번 초과하여 더해질 수 없는 것
# ex) 2 4 5 4 6 으로 이루어진 배열이 있을 때 m이 8이고 k가 3일 때 특정한 인덱스의 수가 연속해서
# 세번까지 더해질 수 있으므로 큰수의 법칙에 따른 결과 6+6+6+5+6+6+6+5

n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)