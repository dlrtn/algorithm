class MostReceivedGift:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        for i in range(n):
            right = right.next

        if not right:
            head = head.next
        else:
            while right.next:
                left = left.next
                right = right.next
            left.next = left.next.next

        return head