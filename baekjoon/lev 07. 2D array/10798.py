answer = []
for i in range(5):
    string = input()

    answer.append(list(string))

for i in range(15):
    for j in range(5):
        if i < len(answer[j]):
            print(answer[j][i], end='')