def solution(myString, pat):
    last = 0
    first = myString.index(pat)

    for i in range(first, myString.count(pat) + first):
        last = myString[i:].index(pat) + i

    last += len(pat)

    return myString[:last]
