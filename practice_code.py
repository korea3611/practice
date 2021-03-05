data = [int(input()) for _ in range(9)]

for a in range(9):
    for b in range(1,9):
        for c in range(2,9):
            for d in range(3,9):
                for e in range(4,9):
                    for f in range(5,9):
                        for g in range(6,9):
                            if data[a]+data[b]+data[c]+data[d]+data[e]+data[f]+data[g] == 100:
                                a = [data[a],data[b],data[c],data[d],data[e],data[f],data[g]]
                                for i in sorted(a):
                                    print(i)
                                exit(0)