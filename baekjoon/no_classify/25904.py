a, b = map(int, input().split())

arr = list(map(int, input().split()))

i = 0

while arr[i % len(arr)] >= b:
    i+=1
    b+=1
    print(b)

print(i % len(arr) + 1)
