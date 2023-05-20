def solution(date1, date2):
    data1 = date1[0] * 365 + date1[1] * 30 + date1[2]
    data2 = date2[0] * 365 + date2[1] * 30 + date2[2]

    if data1 < data2:
        return 1

    return 0
