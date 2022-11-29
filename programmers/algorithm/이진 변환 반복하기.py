def solution(s):
    count = 0
    n = 0
    while True:
        count += s.count('0')
        print(bin(s.count('1'))[2:])
        s = bin(s.count('1'))[2:]
        n += 1
        if s == '1':
            break
    return [n, count]