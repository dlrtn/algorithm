# how to get a, b, c with space in between?
# a, b, c = map(int, input().split())

grade_sum = 0
time_sum = 0


for i in range(20):
    name, time, grade = input().split()

    if grade == 'A+':
        grade_sum += 4.5 * float(time)
    elif grade == 'A0':
        grade_sum += 4.0 * float(time)
    elif grade == 'B+':
        grade_sum += 3.5 * float(time)
    elif grade == 'B0':
        grade_sum += 3.0 * float(time)
    elif grade == 'C+':
        grade_sum += 2.5 * float(time)
    elif grade == 'C0':
        grade_sum += 2.0 * float(time)
    elif grade == 'D+':
        grade_sum += 1.5 * float(time)
    elif grade == 'D0':
        grade_sum += 1.0 * float(time)
    elif grade == 'F':
        grade_sum += 0.0 * float(time)

    if grade == 'P':
        time_sum += 0
    else:
        time_sum += float(time)

print(round(grade_sum / time_sum, 6))