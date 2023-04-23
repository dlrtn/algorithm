def solution(myString):
    myString = myString.lower()

    while True:
        if 'a' not in myString:
            break
        myString = myString.replace('a', 'A')
    return myString
