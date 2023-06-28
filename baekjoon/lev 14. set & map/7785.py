num = int(input())
dict = {}
name_list = []
for i in range(num):
    name, status = input().split()

    if status == 'enter':
        dict[name] = status

    elif status == 'leave':
        del dict[name]

for i in dict.keys():
    name_list.append(i)

name_list.sort(reverse=True)
print('\n'.join(name_list))
