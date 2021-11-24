a, b = map(int, input().split())
dic = {}
for i in range(a):
    x, y = map(str, input().split())
    dic[x] = y
print(dic)
for i in range(b):
    temp = input()
    print(dic[temp])