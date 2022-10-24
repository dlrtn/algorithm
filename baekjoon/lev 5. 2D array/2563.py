arr = [[0]* 100]* 100

n = int(input())

abb = set()

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, a + 10):
        for k in range(b, b + 10):
            abb.add(str(j)+","+str(k))

print(len(abb))