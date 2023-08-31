N = int(input())

first = 1
second = 1

for i in range(N):
    if i < 2:
        print(1, end=' ')
        continue

    third = first + second
    print(third, end=' ')

    if i % 9 == 0:
        print()

    first = second
    second = third
