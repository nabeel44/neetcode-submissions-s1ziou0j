# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 1 2 3 4 5 6 7
# 0 6 1 2 3 4 5
# 0 6 1 5 2 3 4
# 0 6 1 5 2 4 3



# 0 6 1 5 2 4 3


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        l, r = 0, len(nodes) - 1
        while l <= r:
            nodes[l].next = nodes[r]
            l += 1
            if l >= r:
                break
            nodes[r].next = nodes[l]
            r -= 1
        nodes[r].next = None
        






        