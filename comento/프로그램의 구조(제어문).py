## if 문
money = True
if money:
    print("택시틀 타고 가라")
else:
    print("걸아가라")

x = 3
y = 2
print(x > y)
print(x < y)
print(x != y)

money = 2000
if money >= 3000:
    print("택시를 타고가라")
else:
    print("걸어가라")

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print(1 in [1,2,3])
print(1 not in [1,2,3])
print('a' in ['a','b','c'])
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고가라")
else:
    print("걸어가라")

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

score = 0
if score >= 60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"

## while문
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다")

number = 0
prompt = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

### for 문문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

a = range(10)
print(a)

add = 0
for i in range(1, 11):
    add = add + i
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)