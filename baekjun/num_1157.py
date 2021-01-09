text = input()
alpabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = text.lower()
text_num_list = []
cnt = 0

for i in alpabet_list:
    cnt = 0
    for y in text:
        if y == i:
            cnt += 1
    text_num_list.append(cnt)

###현재 text_num_list = [````````````````]
if text_num_list.count(max(text_num_list)) >= 2:
    print("?")
else:
    print(alpabet_list[text_num_list.index(max(text_num_list))].upper())
