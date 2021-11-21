n = input()
cnt = 0
a = []
if n == '0':
    print(0)
    exit()

if n[0] == '0':
    pass
elif n[0] == '1':
    a.append('1')
elif n[0] == '2':
    a.append('10')
elif n[0] == '3':
    a.append('11')
elif n[0] == '4':
    a.append('100')
elif n[0] == '5':
    a.append('101')
elif n[0] == '6':
    a.append('110')
elif n[0] == '7':
    a.append('111')

for i in n[1:]:
    if i == '0':
        a.append('000')
    elif i == '1':
        a.append('001')
    elif i == '2':
        a.append('010')
    elif i == '3':
        a.append('011')
    elif i == '4':
        a.append('100')
    elif i == '5':
        a.append('101')
    elif i == '6':
        a.append('110')
    elif i == '7':
        a.append('111')

print("".join(a))