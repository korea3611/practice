dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a = {1:'a'}
a[2] = 'b'
print(a)

# 딕셔너리 요소 삭제시 에는
del a[1]
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

## 딕셔너리 만들 때 주의사항
 # : 딕셔너리에서 key는 고유한 값이므로 중복되는 key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점을 주의해야함

print(dic.keys())
list(dic.keys())
dic.clear()
