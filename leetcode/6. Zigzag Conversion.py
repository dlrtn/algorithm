class MostReceivedGift:
    def convert(self, s: str, numRows: int) -> str:
        n = 2 * numRows - 2
        print(n)

        answerArr = ''

        if numRows == 1:
            return s

        for i in range(numRows):
            term = n - 2 * i
            print(numRows, term)

            count = 0
            nowIndex = i
            if i == 0 or i == numRows - 1:
                while True:
                    if nowIndex >= len(s):
                        break

                    answerArr += s[nowIndex]
                    count += 1

                    nowIndex += n

            else:
                while True:
                    if nowIndex >= len(s):
                        break

                    answerArr += s[nowIndex]
                    count += 1

                    if count % 2 == 0:
                        nowIndex += n - term
                    else:
                        nowIndex += term
        return answerArr
