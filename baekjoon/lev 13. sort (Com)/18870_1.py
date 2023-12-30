import sys

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

non_duplicated_numb_list = sorted(set(num_list))
num_dict = {}

for i in range(len(non_duplicated_numb_list)):
    num_dict[non_duplicated_numb_list[i]] = i

answer_list = []
for i in num_list:
    answer_list.append(num_dict[i])

print(*answer_list)
