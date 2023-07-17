n = 1
dict = {
    '1': 2,
    '2': 3,
    '3': 3,
    '4': 3,
    '5': 3,
    '6': 3,
    '7': 3,
    '8': 3,
    '9': 3,
    '0': 4
}

while True:
    n = list(input())

    if n == ['0']:
        break
    s = 0
    for i in n:
        s += dict[i]
    s += len(n) + 1

    print(s)
