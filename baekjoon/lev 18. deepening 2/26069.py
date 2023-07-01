n = int(input())

dance = {'ChongChong'}
for i in range(n):
    a, b = input().split()

    if a in dance:
        dance.add(b)

    elif b in dance:
        dance.add(a)


print(len(dance))