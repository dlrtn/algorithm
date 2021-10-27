n = input()
cnt = 1
a = []
for i in range(len(n)):
    a.append((int(n) // cnt) % 10)
    cnt *= 10
a.sort()
a.reverse()
for i in a:
    print(i, end = '')