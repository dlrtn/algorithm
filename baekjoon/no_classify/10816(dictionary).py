import sys

N = int(sys.stdin.readline().rstrip())
N_array = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
M_array = list(map(int, sys.stdin.readline().rstrip().split()))

N_array.sort()

N_dict = dict()
for i in N_array:
    if i in N_dict.keys():
        N_dict[i] += 1
    else:
        N_dict[i] = 1

for i in M_array:
    if i in N_dict.keys():
        print(N_dict[i], end=' ')
    else:
        print(0, end=' ')