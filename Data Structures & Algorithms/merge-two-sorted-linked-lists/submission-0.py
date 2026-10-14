# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0, 1, 2] -> [2, 1, 0]
# prev = none (0)
# temp = curr.next (1)
# curr.next = prev
# prev = curr
# curr = temp
# 
# put 


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

            


