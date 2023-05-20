def solution(priorities, location):
    N = len(priorities)

    while True:
        if len(priorities) == 1:
            break

        now = priorities.pop(0)

        if now < max(priorities):
            location -= 1
            priorities.append(now)

        print(priorities)

    if location < 0:
        return N + 1 + location
    else:
        return location + 1
