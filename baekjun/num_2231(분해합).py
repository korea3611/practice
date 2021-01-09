def maker(n):
    for i in range(n):
        num = str(i)
        total = i
        for j in num:
            total += int(j)
        if total == n:
            return i
    return 0


n = int(input())
print(maker(n))


