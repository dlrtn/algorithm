a,b = map(int,input().split())

set_m = set()
list_s = []

for i in range(a):
    set_m.add(input())


for i in range(b):
    list_s.append(input())

count = 0
for i in list_s:
    if i in set_m:
        count += 1

print(count)


