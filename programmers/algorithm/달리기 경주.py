def solution(players, callings):
    # 선수: 위치
    player_stat = {j: i for i, j in enumerate(players)}
    # 위치: 선수
    stat_player = {i: j for i, j in enumerate(players)}

    for call in callings:
        a = player_stat[call]
        pre_idx = a - 1
        x = call
        y = stat_player[pre_idx]

        player_stat[x] = pre_idx
        player_stat[y] = a

        stat_player[pre_idx] = x
        stat_player[a] = y

    return list(stat_player.values())
