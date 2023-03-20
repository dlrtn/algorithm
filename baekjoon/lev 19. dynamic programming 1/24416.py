n = int(input())

arr_rec = [0, 1, 1, 2, 3, 5]

for i in range(6, n+1):
    arr_rec.append(arr_rec[i-1] + arr_rec[i-2])

print(arr_rec[n], n-2)