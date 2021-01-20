# 2-1 정수형
a = 123
a = -178
a = 0

# 실수형
a = 1.2
a = -3.45
a = 4.24E10
a = 4.24e-10

# 8진수와 16진수
a = 0o177
a = 0x8ff
b = 0xABC

# 사칙연산
a = 3
b = 4
print(a+b)
print(a*b)
print(a/b)
print(a**b)

print(7%3)
print(3%7)
print(7/4)
print(7//4)

## 문자열
"Hello world"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

food = "Python's favorite food is perl"
say = '"Python is very easy." he says.'
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
multiline = "Life is too short\nYou need python"
head = "Python"
tail = " is fun!"
print(head + tail)
a = "python"
print(a * 2)
print("=" * 50)
print("My Program")
print("=" * 50)
a = "Life is too short"
print(len(a))

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
a = "Life is too short, You need Python"
print(a[0:4])

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

print("I eat %d apples." % 3)
print("I eat %s apples." % "five")

number = 3
print("I eat %d apples." % number)

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age = 30
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

a = "hi"
print(a.upper())
a = "HI"
print(a.lower())

a = " hi "
print(a.lstrip())
a= " hi "
print(a.rstrip())

a = " hi "
print(a.strip())
a = "Life is too short"
print(a.replace("Life", "Your leg"))

a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':'))