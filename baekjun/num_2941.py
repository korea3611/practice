li = ['c=','c-','dz=','d-','lj','nj','s=','z=']

text = input()

for i in li:
    text = text.replace(i,'*')

print(len(text))
