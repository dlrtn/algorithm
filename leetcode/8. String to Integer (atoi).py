class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s)
        while s and s[0] == ' ':
            s.pop(0)

        oper = 1

        if s and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                oper = -1
            s.pop(0)

        temp = []

        for i in s:
            if i.isdigit():
                temp.append(i)
            else:
                break

        while s and s[0] == 0:
            s.pop(0)

        temp = ''.join(temp)

        if temp != '' and int(temp) > 2147483647:
            if oper == 1:
                return 2147483647
            else:
                return -2147483648

        if temp:
            return int(temp) * oper
        else:
            return 0