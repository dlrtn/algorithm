def solution(bridge_length, weight, truck_weights):
    answer = 0
    weight_sum = 0
    truck_start = list()
    count = 0

    while truck_weights:
        for i in range(len(truck_start)):
            if count - truck_start[i][1] == bridge_length:
                weight_sum -= truck_start[i][0]

        if weight >= weight_sum + truck_weights[0]:
            now_start_truck_weight = truck_weights.pop(0)
            truck_start.append((now_start_truck_weight, count))
            weight_sum += now_start_truck_weight

        count += 1

    return count + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
