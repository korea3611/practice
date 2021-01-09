a= input()
a_list = list(a)
alpabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



for i in alpabet_list:
    if i in a_list:
        print(a_list.index(i))
    else:
        print(-1)

