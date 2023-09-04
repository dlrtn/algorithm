import sys


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


n = int(sys.stdin.readline().rstrip())

minus_list = []
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

for i in range(n - 1):
    minus_list.append(arr[i + 1] - arr[i])

min_num = gcd(minus_list[0], minus_list[1])
for i in range(2, len(minus_list)):
    min_num = gcd(min_num, minus_list[i])

print((arr[-1] - arr[0]) // min_num - n + 1)
