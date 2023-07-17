N = int(input())

s = list(map(int, input().split()))

su = 0

disk = int(input())

dis = 0
for i in s:
    if i == 0:
        continue
    else:
        if i % disk == 0:
            dis += i // disk
        else:
            dis += i // disk + 1

print(dis * disk)
