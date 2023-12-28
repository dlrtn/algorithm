def solution(bandage, health, attacks):
    answer = 0
    start_time = attacks[0][0]
    end_time = attacks[-1][0]
    now_health = health - attacks.pop(0)[1]
    next_attack = attacks.pop(0)
    bandage_count = 0

    for i in range(start_time, end_time):
        if i == next_attack[0] - 1:
            now_health -= next_attack[1]
            if len(attacks) > 0:
                next_attack = attacks.pop(0)
            bandage_count = 0
        else:
            bandage_count += 1
            now_health += bandage[1]

        if now_health <= 0:
            return -1

        if bandage_count == bandage[0]:
            bandage_count = 0
            now_health += bandage[2]

        if now_health > health:
            now_health = health


    return now_health

 