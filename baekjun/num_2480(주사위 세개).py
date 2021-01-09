n_list = list(map(int,input().split()))

if len(set(n_list)) == 1:
    print(max(n_list)*1000+10000)
elif len(set(n_list)) == 2:
    for n in n_list:
        if n_list.count(n) == 2:
            print(1000+n*100)
            exit()
else:
    print(max(n_list)*100)