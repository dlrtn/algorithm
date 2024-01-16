from itertools import permutations

def solution(k, dungeons):
    max_completed = 0

    for permutation in permutations(dungeons):
        current_health = k
        count = 0

        for dungeon in permutation:
            required_health, health_cost = dungeon

            if current_health >= required_health:
                current_health -= health_cost
                count += 1
            else:
                break

        max_completed = max(max_completed, count)

    return max_completed
