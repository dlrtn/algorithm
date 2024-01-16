class MostReceivedGift:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        answerLen = []

        for i in range((n + m) // 2 + 1):
            if len(nums1) == 0:
                answerLen.append(nums2.pop(0))
                continue

            if len(nums2) == 0:
                answerLen.append(nums1.pop(0))
                continue

            if nums1[0] > nums2[0]:
                answerLen.append(nums2.pop(0))
            else:
                answerLen.append(nums1.pop(0))

        print(answerLen)

        if (n + m) % 2 == 0:
            return (answerLen[-1] + answerLen[-2]) / 2

        else :
            return answerLen[-1]