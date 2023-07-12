import math


def solution(fees, records):
    data = {}

    for record in records:
        time, car_number, action = record.split()
        minutes = int(time[:2]) * 60 + int(time[3:5])

        if car_number not in data:
            data[car_number] = []

        data[car_number].append([minutes, action])

    answer = []

    for car_number, actions in data.items():
        total_time = 0

        for i in range(0, len(actions), 2):
            in_time = actions[i][0]
            out_time = actions[i + 1][0] if i + 1 < len(actions) else 1439
            total_time += out_time - in_time

        additional_time = max(0, total_time - fees[0])
        additional_fee = math.ceil(additional_time / fees[2]) * fees[3]
        price = fees[1] + additional_fee
        answer.append((car_number, price))

    answer.sort(key=lambda x: x[0])
    sorted_prices = [price for _, price in answer]

    return sorted_prices
