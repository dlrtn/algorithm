n = int(input())
a = []
for i in range(n):
    temp = int(input())
    if temp == 0:
        a.remove(a[-1])
    else:
        a.append(temp)
print(sum(a))