class MostReceivedGift:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = {'(', '[', '{'}
        closing_brackets = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in opening_brackets:
                stack.append(i)
            elif i in closing_brackets:
                if len(stack) == 0 or stack[-1] != closing_brackets[i]:
                    return False
                stack.pop()
            else:
                return False

        return len(stack) == 0
