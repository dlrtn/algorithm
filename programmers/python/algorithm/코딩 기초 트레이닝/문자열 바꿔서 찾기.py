def solution(myString, pat):
    mS = ''
    ans = ''

    for i in myString:
        if i == 'B':
            mS += '1'
        else:
            mS += '0'

    for i in pat:
        if i == 'A':
            ans += '1'
        else:
            ans += '0'

    if ans in mS:
        return 1
    return 0