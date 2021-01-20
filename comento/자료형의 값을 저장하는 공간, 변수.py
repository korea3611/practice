a = [1,2,3]
print(id(a))

# 리스트를 복사하고자 할 때

# 이렇게 하면 id 값이 동일하게 나옴
b = a
print(a is b)

# a 를 바꾸면 b 도 바뀜, 동일한 id 값을 가지고 있기 때문

# 1. [:] 이용하기
a = [1,2,3]
b = a[:]
a[1] = 4
print(a,b)

# 2. copy 모듈 사용
from copy import copy
b = copy(a)

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a,b] = ['python', 'life']
a = b = 'python'

# 두 변수의 값을 간단히 바꾸는 방법
a = 3
b = 5
a,b = b,a
print(a,b)