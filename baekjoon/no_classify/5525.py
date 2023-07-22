N = int(input())
M = int(input())
S = input()

P = ''

for i in range(2 * N + 1):
    if i % 2 == 0:
        P += 'I'
    else:
        P += 'O'

count = 0

for i in range(M - 2 * N):
    if P == S[i:i + 2 * N + 1]:
        count += 1

print(count)
