import sys

now_kg = int(sys.stdin.readline())
item_list = []
for i in range(3):
    item_list.append(list(map(str, sys.stdin.readline().split(', '))))

for i in range(3):
    item_list[i][1] = int(item_list[i][1])
    item_list[i][2] = int(item_list[i][2][:-1])

available_kg = 20 - now_kg

item_list.sort(key=lambda x: x[1], reverse=True)

answer = []
for i in range(3):
    if available_kg >= item_list[i][2]:
        answer.append(item_list[i][0])
        available_kg -= item_list[i][2]

print(answer)
