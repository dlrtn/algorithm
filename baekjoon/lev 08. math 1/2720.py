n = int(input())

for i in range(n):
    temp = int(input())

    quarter = temp // 25
    temp %= 25
    dime = temp // 10
    temp %= 10
    nickel = temp // 5
    temp %= 5
    penny = temp // 1
    temp %= 1

    print(quarter, dime, nickel, penny)
