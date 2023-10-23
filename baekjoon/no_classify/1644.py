import sys

N = int(sys.stdin.readline().rstrip())

prime_array = []


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


for i in range(2, N + 1):
    if is_prime(i):
        prime_array.append(i)

cur_sum = [0 for _ in range(len(prime_array) + 1)]

for i in range(1, len(prime_array) + 1):
    cur_sum[i] += prime_array[i - 1] + cur_sum[i - 1]

count = 0
left = 0
right = len(prime_array)

while right <= len(prime_array):

    ans = cur_sum[right] - cur_sum[left]
    if ans == N:
        left += 1
        right += 1
        count += 1
    elif ans < N:
        left += 1
        right += 1
    else:
        right -= 1

print(count)
