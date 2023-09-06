N = int(input())

input_list = list(map(int, input().split()))

value, index = map(int, input().split())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


for i in range(N):
    if i == 0:
        head = Node(input_list[i])
        current = head
    else:
        current.next = Node(input_list[i])
        current = current.next

find = head

for i in range(index - 1):
    find = find.next

next_node = find.next
find.next = Node(value)
find.next.next = next_node

while head is not None:
    print(head.data, end=" ")
    head = head.next
