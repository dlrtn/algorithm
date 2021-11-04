n = int(input())
str = [i for i in range(1, n+1)]
while True:
    if len(str) == 1:
        break
    str.pop(0)
    str.append(str.pop(0))
print(str[0])