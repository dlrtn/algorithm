def solution(cacheSize, cities):
    answer = 0
    arr = []
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        if i.lower() not in arr and cacheSize > len(arr):
            arr.append(i.lower())
            answer += 5
        elif i.lower() not in arr and cacheSize == len(arr):
            del arr[0]
            arr.append(i.lower())
            answer += 5
        else:
            del arr[arr.index(i.lower())]
            arr.append(i.lower())
            answer += 1

    return answer
