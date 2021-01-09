class Foo:
    class Bar():
        @staticmethod
        def func():
            print("C")


    def __init__(self):
        pass

    @staticmethod
    def bar():
        print("A")

    @staticmethod
    def func():
        print("B")


    def __str__(self):
        return "D"




Foo.bar()
Foo().func()
Foo.Bar.func()
print(Foo())