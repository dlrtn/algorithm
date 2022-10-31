from fractions import Fraction

n = int(input())

arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    temp = Fraction(arr[i],arr[0])
    print("{}/{}".format(temp.denominator, temp.numerator))