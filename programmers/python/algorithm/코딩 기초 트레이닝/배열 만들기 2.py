def solution(l, r):
    result = []
    for i in range(l, r + 1):
        if '1' in str(i):
            continue
        elif '2' in str(i):
            continue
        elif '3' in str(i):
            continue
        elif '4' in str(i):
            continue
        elif '6' in str(i):
            continue
        elif '7' in str(i):
            continue
        elif '8' in str(i):
            continue
        elif '9' in str(i):
            continue
        else:
            result.append(i)
    if len(result) == 0:
        return [-1]

    return result
