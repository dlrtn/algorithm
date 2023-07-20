answer = [0 for _ in range(100000)]

print(answer)
for i in range(1, 6):
    count = i
    if i == 1:
        while count < 10001:
            answer[count] = i
            count += 8

    if i == 2:
        while count < 10001:
            answer[count] = i
            count

print(answer)