## 함수
def 함수명(매개변수):
    pass

def add(a,b):
    return a + b

a = 3
b = 4
c = add(a,b)
print(c)

def add(a,b):
    result = a+b
    return result

a = add(3,4)
print(a)

def say():
    return 'Hi'
a = say()
print(a)

result = add(a = 3, b = 7)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul',1,2,3,4,5)
print(result)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name = 'foo', age = 3)

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)
result1, result2 = add_and_mul(3,4)

## return 문은 한번만 실행된다

def say_nick(nick):
    if nick =='바보':
        return
    print("나의 별명은 %s 입니다"  % nick)

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)

a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)

def vartest(hello):
    hello = hello + 1

a = 1
def vartest(a):
    a = a +1
    return a

a = vartest(a)
print(a)

a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)

add = lambda a, b : a+b
result = add(3,4)
print(result)

def add(a,b):
    return a+b

result = add(3,4)
print(result)

## 사용자 입력과 출력
a = input()
number = input("숫자를 입력하세요: ")

a = 123
print(a)
a = 'python'
print(a)
a = [1,2,3]
print(a)

print("life" "is" "too short")
print("life" + "is" + "too short")
print("life","is","too short")

for i in range(10):
    print(i, end=' ')

### 파일 읽고 쓰기
f = open("새파일.txt", 'w')
f.close()

f = open("C:/doit/새파일.txt", 'w')
f.close()

f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)

f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

import sys

args = sys.argv[1:]
for i in args:
    print(i)