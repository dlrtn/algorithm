def solution(my_string):
    while True:
        if '  ' not in my_string:
            break
        my_string = my_string.replace('  ', ' ')
    return my_string.strip().split(' ')
