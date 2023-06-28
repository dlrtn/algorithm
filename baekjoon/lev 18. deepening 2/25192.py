n = int(input())


chatting_list = []
temp_list = []
for i in range(n):
    chatting = input()

    if chatting == 'ENTER':
        if len(temp_list) != 0:
            chatting_list.append(set(temp_list))
        temp_list = []
    else:
        temp_list.append(chatting)
chatting_list.append(set(temp_list))

count = 0

for i in chatting_list:
    count += len(i)

print(count)
