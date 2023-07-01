a, b = map(int, input().split())

dict = {}
for i in range(a):
    s = input()

    if len(s) < b:
        continue

    else:
        if s not in dict.keys():
            dict[s] = 1
        else:
            dict[s] += 1

dict = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in dict:
    print(i[0])
