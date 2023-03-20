def solution(polynomial):
    x_count = 0
    c_count = 0

    for i in polynomial.split(" + "):
        if i[-1] == 'x':
            if len(i) > 1:
                x_count += int(i[:-1])
            else:
                x_count += 1
        else:
            c_count += int(i)

    if c_count == 0:
        if c_count == 0:
            return "{}x".format(x_count)
        return "x"
    elif x_count == 0:
        return "{}".format(c_count)
    elif x_count == 1:
        return "x + {}".format(c_count)
    else:
        return "{}x + {}".format(x_count, c_count)
