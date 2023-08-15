import sys

N, M = map(int, sys.stdin.readline().split())
know = set(list(map(int, sys.stdin.readline().split()))[1:])
party_list = []
for _ in range(M):
    party_list.append(list(map(int, sys.stdin.readline().split()))[1:])

for _ in range(M):
    for party in party_list:
        if know & set(party):
            know |= set(party)

count = 0

for party in party_list:
    isTrue = False
    for member in party:
        if member in know:
            isTrue = True

    if not isTrue:
        count += 1

print(count)
