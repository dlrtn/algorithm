answer = ""

for i in range(3):
    now = input()

    if i < 2:
        if "black" == now:
            answer += "0"
        if "brown" == now:
            answer += '1'
        if "red" == now:
            answer += '2'
        if "orange" == now:
            answer += '3'
        if "yellow" == now:
            answer += '4'
        if "green" == now:
            answer += '5'
        if "blue" == now:
            answer += '6'
        if "violet" == now:
            answer += '7'
        if "grey" == now:
            answer += '8'
        if "white" == now:
            answer += '9'
    else :
        if "black" == now:
            1
        if "brown" == now:
            answer += '0'
        if "red" == now:
            answer += '00'
        if "orange" == now:
            answer += '000'
        if "yellow" == now:
            answer += '0000'
        if "green" == now:
            answer += '00000'
        if "blue" == now:
            answer += '000000'
        if "violet" == now:
            answer += '0000000'
        if "grey" == now:
            answer += '00000000'
        if "white" == now:
            answer += '000000000'

if answer[0] == '0' and answer[1] == '0':
    print('0')
elif answer[0] == '0':
    print(answer[1:])
else :
    print(answer)
