# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 1 2 3 4 5 6 7
# 0 6 1 2 3 4 5
# 0 6 1 5 2 3 4
# 0 6 1 5 2 4 3



# 0 -> 1 -> 2 -> 3 ->

# 2 -> 1 -> 0



# 4 3 2 1 0


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # midpoint is slow, reverse after it
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        l1, l2 = head, prev
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l1 = l1.next
            l1.next = tmp1
            l1 = l1.next
            l2 = tmp2
        