import itertools
import sys

N = int(sys.stdin.readline().rstrip())
S = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
player_list = [i for i in range(1, N + 1)]

player_com_list = list(itertools.combinations(player_list, N // 2))

for i in range(N):
    for j in range(N):
        S[j][i] += S[i][j]

min_gap = sys.maxsize
answer = 0
for i in player_com_list:
    start_overall = 0
    link_overall = 0

    if i[0] == 1:
        start_team = list(i)
        link_team = list()
        for x in range(1, N + 1):
            if x not in start_team:
                link_team.append(x)

        for j in range(N // 2):
            for k in range(j + 1, N // 2):
                start_overall += S[start_team[k] - 1][start_team[j] - 1]
                link_overall += S[link_team[k] - 1][link_team[j] - 1]
        answer = min(abs(start_overall - link_overall), min_gap)
        min_gap = answer

print(answer)
