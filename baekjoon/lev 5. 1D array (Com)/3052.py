a = []
for i in range(10):
    temp = int(input())
    if temp % 42 not in a:
        a.append(temp % 42)

print(len(a))