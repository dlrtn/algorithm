class MostReceivedGift:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        word1_list = list(word1)
        word2_list = list(word2)
        temp = ''
        while True:
            if len(word1_list) == 0 and len(word2_list) == 0:
                break

            if len(word1_list) == 0:
                temp += word2_list.pop(0)

            elif len(word2_list) == 0:
                temp += word1_list.pop(0)

            elif count % 2 == 0:
                temp += word1_list.pop(0)

            else:
                temp += word2_list.pop(0)

            count += 1


        return temp
