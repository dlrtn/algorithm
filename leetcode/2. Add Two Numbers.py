# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        while True:
            list1.append(str(l1.val))
            if l1.next == None:
                break

            l1 = l1.next

        while True:
            list2.append(str(l2.val))
            if l2.next == None:
                break

            l2 = l2.next

        num1 = int(''.join(reversed(list1)))
        num2 = int(''.join(reversed(list2)))

        dummy = ListNode()
        curr = dummy

        for digit in reversed(str(num1 + num2)):
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
