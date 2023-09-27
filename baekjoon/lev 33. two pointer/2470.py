import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

i, j = 0, len(a) - 1

min_val = sys.maxsize

answer_i, answer_j = 0, 0

count = 0
while i < j:
    if a[i] + a[j] == 0:
        answer_i, answer_j = i, j
        break
    elif a[i] + a[j] > 0:
        if abs(a[i] + a[j]) < min_val:
            answer_i, answer_j = i, j
            min_val = abs(a[i] + a[j])
        j -= 1
    else:
        if abs(a[i] + a[j]) < min_val:
            answer_i, answer_j = i, j
            min_val = abs(a[i] + a[j])
        i += 1

print(a[answer_i], a[answer_j])
