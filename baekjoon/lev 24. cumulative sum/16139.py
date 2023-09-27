import sys

S = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())

alpha = dict()

for i in range(ord('a'), ord('z') + 1):
    alpha[chr(i)] = [[0] * len(S) for _ in range(len(S))]

for i in alpha.keys():
    for j in range(len(S)):
        for k in range(j, len(S)):
            if S[k] == i:
                alpha[i][j][k] += 1

for i in alpha.keys():
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            alpha[i][j][k] += alpha[i][j][k - 1]

for i in range(q):
    a, l, r = sys.stdin.readline().split()

    print(alpha[a][int(l)][int(r)])
