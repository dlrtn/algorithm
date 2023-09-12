import sys

input_list = list(map(int, sys.stdin.readline().split()))

print(input_list)

coin_count = int(input_list[0])
money = int(input_list[-1])
item_price = int(input_list[-2])
coin_list = input_list[1: coin_count + 2]

change = money - item_price

answer_list = [0] * coin_count

for i in range(coin_count):
    answer_list[i] = change // coin_list[i]
    change -= answer_list[i] * coin_list[i]

print(answer_list)
