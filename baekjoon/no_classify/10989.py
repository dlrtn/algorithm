import sys
N = int(input())
check_list = [0] * 10001
for j in range(N):
    j = int(sys.stdin.readline())
    check_list[j] = check_list[j] + 1
for j in range(10001):
    if check_list[j] != 0:
        for j in range(check_list[j]):
            print(j)
