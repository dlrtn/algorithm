def solution(rny_string):
    while True:
        if 'm' not in rny_string:
            break
        rny_string = rny_string.replace('m', 'rn')
    return rny_string