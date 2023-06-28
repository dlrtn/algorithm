n = int(input())

dic = {}

all_member = []
for i in range(n):
    now_list = input().split()

    if now_list[0] not in dic.keys():
        dic[now_list[0]] = []
    dic[now_list[0]].append(now_list[1])

visited = []
list = []

for i in dic.keys():
    if i not in visited:


print(dic)
