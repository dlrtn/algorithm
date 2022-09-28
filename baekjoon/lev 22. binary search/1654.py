a, b = map(int, input().split())
c = []
for i in range(a):
    c.append(int(input()))
left = 1
right = max(c)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in range(a):
        total += c[i] // mid

    if total >= b:
        left = mid + 1
    else:
        right = mid - 1

print(right)