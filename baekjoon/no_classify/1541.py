string = input()


def convert_to_list(input_string):
    result_list = []

    current_number = ""
    for char in input_string:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                result_list.append(int(current_number))
                current_number = ""
            result_list.append(char)

    if current_number:
        result_list.append(int(current_number))

    return result_list


result = convert_to_list(string)
answer = 0
sep = True
for i in range(len(result)):
    if str(result[i]).isdigit():
        if sep:
            answer += result[i]
        else:
            answer -= result[i]
    else:
        if result[i] == '-':  # sep = !sep
            sep = False

print(answer)
