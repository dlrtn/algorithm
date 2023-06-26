class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-10001)  # 더미 노드를 사용하여 헤드 노드를 가리킴
        answer = dummy
        while True:
            min_num = 10001
            now_index = -1  # 현재 노드의 인덱스를 저장하는 변수
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_num:
                    now_index = i
                    min_num = lists[i].val
            if min_num == 10001:
                break
            new_node = ListNode(min_num)
            answer.next = new_node
            answer = answer.next
            lists[now_index] = lists[now_index].next
        return dummy.next  # 더미 노드의 다음 노드부터 반환
