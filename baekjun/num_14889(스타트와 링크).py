from itertools import combinations
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
members = [i for i in range(n)]
possible_team = []

#조합으로 가능한 팀 생성
for team in list(combinations(members, n//2)):
    possible_team.append(team)

min_stat_gap = 10000
for i in range(len(possible_team) // 2):
    team = possible_team[i]
    stat_A = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_A += data[member][k]

    team = possible_team[-i-1]
    stat_B = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_B += data[member][k]

    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))

print(min_stat_gap)

