def solution(my_string, alp):
    while True:
        if alp not in my_string:
            break
        my_string = my_string.replace(alp, alp.upper())
    return my_string
