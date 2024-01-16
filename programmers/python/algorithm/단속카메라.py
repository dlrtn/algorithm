def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])

    gosokdoro = routes[0][1]
    # [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    for i in range(1, len(routes)):
        if routes[i][0] <= gosokdoro:
            continue
        else:
            gosokdoro = routes[i][1]
            answer += 1

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
