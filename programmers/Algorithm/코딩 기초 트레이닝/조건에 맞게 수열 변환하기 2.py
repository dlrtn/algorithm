def solution(arr):
    answer = 0
    flag = False
    while True:

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
                flag = True
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
                flag = True

        if flag == False:
            break
        else:
            answer += 1

        flag = False

    return answer
