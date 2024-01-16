class MostReceivedGift:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(now_string, remaining_digits):
            if not remaining_digits:
                answer_list.append(now_string)
                return

            for char in mapping[remaining_digits[0]]:
                dfs(now_string + char, remaining_digits[1:])

        answer_list = []
        dfs('', digits)

        if answer_list[0] == "":
            return []
        return answer_list



