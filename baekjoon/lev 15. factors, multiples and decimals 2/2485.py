n = int(input())

min = []
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(n - 1):
    min.append(arr[i + 1] - arr[i])

min.sort()

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

min_num = gcd(min[0], min[1])
for i in range(1, len(min) - 1):
    min_num = gcd(min[i], min_num)
print(min_num)
print((arr[-1] - arr[0]) // min_num - n + 1)
