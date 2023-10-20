import itertools
import sys

short_peoples = []
for i in range(9):
    short_peoples.append(int(sys.stdin.readline().rstrip()))

for i in itertools.combinations(short_peoples, 7):
    if sum(i) == 100:
        for j in sorted(list(i)):
            print(j)
        exit()
