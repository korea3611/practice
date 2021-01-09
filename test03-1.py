def mymap(func, a: list) -> list:
    result = [func(i) for i in a]
    return result

def abc(n):
    print(n)

mymap(abc,[1,2,3,4,5])

