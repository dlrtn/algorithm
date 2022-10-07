str = input()

answer = set()

for i in range(0, len(str)):
    for j in range(len(str)-i):
        answer.add(str[i:i+j+1])
print(len(answer))

