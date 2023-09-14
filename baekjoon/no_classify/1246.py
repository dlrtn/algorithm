import sys

N, M = map(int, sys.stdin.readline().split())

customer_list = []
max_price = 0
max_profit = 0

for _ in range(M):
    customer_list.append(int(sys.stdin.readline()))

customer_list.sort()
M = N if N < M else M
for i in range(1, M + 1):
    now_profit = customer_list[-i] * i
    if now_profit > max_profit:
        max_profit = now_profit
        max_price = customer_list[-i]

print(max_price, max_profit)
