class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        temp = ''
        count = 0
        while True:
            if len(strs[0]) - 1 < count or len(strs[1]) - 1 < count:
                break

            if strs[0][count] == strs[1][count]:
                temp += strs[0][count]
            else:
                break
            count += 1

        for i in range(1, len(strs) - 1):
            temp1 = ''
            count = 0
            while True:
                if len(temp) - 1 < count or len(strs[i + 1]) - 1 < count:
                    break

                if temp[count] == strs[i + 1][count]:
                    temp1 += strs[i + 1][count]
                else:
                    break

                count += 1
            temp = temp1

        return temp
