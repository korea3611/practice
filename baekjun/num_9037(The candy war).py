## 아이들은 동시에 자기가 가지고 있는 사탕의 절반을 오른쪾 아이에게 주고
## 홀수개의 사탕을 가지고 있는 아이가 있을 경우 +1
## 입력의 첫줄은 테스트 케이스의 개수 T
## 각각의 테스트 케이스의 첫줄에서는 아이의 인원 N
## 그 다음줄에는 각 아이들이 초기에 가지고 있는 사탕의 개수
## 아이들은 사이클의 형태로 앉아있음 유의

## 잘모르겠다 (실버 5문제임)

def check(n, candy):
    for i in range(n):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1

def teacher(n, candy):
    tmp_lst = [0 for i in range(n)]
    for idx in range(n):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx+1) % n] = candy[idx]

    for idx in range(n):
        candy[idx] += tmp_lst[idx]

    return candy


def process():
    n, candy = int(input()), list(map(int,input().split()))
    cnt = 0
    while not check(n, candy):
        cnt += 1
        candy = teacher(n, candy)
    print(cnt)

for i in range(int(input())):
    process()


