def solution(myStr):
    while True:
        if 'a' not in myStr and 'b' not in myStr and 'c' not in myStr:
            break

        myStr = myStr.replace('a', ' ')
        myStr = myStr.replace('b', ' ')
        myStr = myStr.replace('c', ' ')

    answer = myStr.split()

    if len(answer) == 0:
        return ["EMPTY"]
    return answer