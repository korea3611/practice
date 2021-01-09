# a = [n for n in range(1,10)]
# print(a)
#
# b = {str(n):'*'*n for n in range(100)}
# print(b)
#
# c = (x**2 for x in [1,10,100,1000,10000])
# print(c)
#
# d = {str(elem) for elem in [52, 32, 15, 62, 34, 27, 45] if elem > 30}
# print(d)

# from functools import partial
# def foo(x=10, y=20, z=5):
#     return x+y+z
#
# print(partial(foo,foo())(10,10))

class A:
    def __init__(self, value):
        self.value = value

    def __mul__(self, x):
        return self.value * x.value

    def __str__(self):
        return 'Value:{}'.format(self.value)

class B:
    def __init__(self,value):
        self.value = value

a = A(100)
b = B(20)
print(a*b)