# 아래와 같은 기능을 가진 Foo 클래스를 완성하시오.
#
# Foo 클래스는 초기화 시 여러개의 정수를 입력으로 받는다. 정수의 개수는 정해져있지 않다. ㅇ
# Foo 클래스의 인스턴스는 print()에 입력될 경우 '입력받은 모든 정수의 합'을 출력한다. ㅇ
# Foo 클래스로 생성된 객체들은 sort를 이용해 정렬할 수 있으며, 정렬할 때에는 '입력받은 모든 정수의 곱'을 기준으로 한다.
# Foo 클래스의 인스턴스끼리 더할 경우, 두 인스턴스의 초기화에 사용된 정수들을 모두 입력받아 생성된 인스턴스를 리턴한다.



class Foo:

    def __init__(self, *args):
        self.li = []
        self.mul_num = 0
        for arg in args:
            self.li.append(arg)
        for i in self.li:
            self.mul_num *= i

    def __str__(self):
        a = sum(self.li)
        return str(a)






foo1 = Foo(1,2,3,4,5)
foo2 = Foo(2,3,4,5,6)
foo3 = Foo(3,4,5,6,7)
print(foo1)
print(foo2)
print(foo3)

li2 = [foo1, foo2, foo3]
sorted(li2)
print(li2)
