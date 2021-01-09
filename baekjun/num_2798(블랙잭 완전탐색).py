##블랙잭

card, sum = map(int,input().split())
# print(card, sum)
card_list = list(map(int, input().split()))
# print(card_list)

result = []

for i in range(card):
    for j in range(i+1, card):
        for k in range(j+1, card):
            if card_list[i] + card_list[j] + card_list[k] > sum:
                continue
            else:
                result.append(card_list[i] + card_list[j] + card_list[k])

print(max(result))

