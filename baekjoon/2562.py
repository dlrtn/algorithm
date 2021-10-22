temp =0
m = 0
for i in range(0,9):
    n = int(input())
    if n>m:
        m=n
        temp = i

print(m)
print(temp+1)