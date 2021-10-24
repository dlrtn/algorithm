a, b = map(int, input().split())
r_a = 0
r_b = 0
r_a = a // 100 + (a // 10 % 10) * 10 + a % 10 * 100
r_a = b // 100 + (b // 10 % 10) * 10 + b % 10 * 100

print(b if r_a < r_b else a)