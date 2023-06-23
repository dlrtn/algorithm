class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(string, left, right, result):
            if left == 0 and right == 0:
                result.append(string)
                return

            if left > 0:
                generate(string + '(', left - 1, right, result)
            if right > left:
                generate(string + ')', left, right - 1, result)

        result = []
        generate('', n, n, result)
        return result
