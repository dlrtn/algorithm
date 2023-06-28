n = int(input())

perfect_squre_number_list = []
i = 1
while True:
    if i ** 2 >= 2200000000:
        break
    perfect_squre_number_list.append(i ** 2)
    i += 1
count = 0

while True:
    if perfect_squre_number_list[count] > n:
        print(count)
        break
    else:
        count += 1

