n = int(input())
str = input()
sum = 0
for i in range(n):
    sum += (26 - (122 - ord(str[i])))*(31**i)
    if sum > 1234567891:
        sum = sum % 1234567891
print(sum)