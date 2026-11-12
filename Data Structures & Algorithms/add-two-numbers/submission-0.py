# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tens = 1
        total = 0
        while l1 and l2:
            first = l1.val * tens
            second = l2.val * tens
            total = total + first + second
            l1, l2 = l1.next, l2.next
            tens *= 10
        while l1:
            first = l1.val * tens
            total += first
            tens *= 10
            l1 = l1.next
        while l2:
            first = l2.val * tens
            total += first
            tens *= 10
            l2 = l2.next
        dummy = ListNode()
        prev = dummy
        strTotal = str(total)
        for i in range(len(strTotal) - 1, -1, -1):
            num = int(strTotal[i])
            curr = ListNode(num)
            prev.next = curr
            prev = curr
        return dummy.next









# 921 
# 421

# 1342

# 1 -> 2 -> 9
# 1 -> 2 -> 4

# 2 + 40 + 1300
# 2 -> 4 -> 3 -> 1