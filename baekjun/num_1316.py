####내코드

n = int(input())
words = []

for i in range(n):
    words.append(list(input()))

for word in words:
    try:
        for i, t in enumerate(word):
            if word[i] == word[i+1]:
                word[i+1] = '*'
    except IndexError:
        continue

cnt = 0

for word in words:
    set_word = set(word)
    if len(word) == len(set_word):
        cnt += 1

print(cnt)

####인터넷 코드
N=int(input())

answer=0

for i in range(N):
    word = input()
    for j in range(len(word)):
        if j!=len(word)-1:
            if word[j]==word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer+=1
print(answer)