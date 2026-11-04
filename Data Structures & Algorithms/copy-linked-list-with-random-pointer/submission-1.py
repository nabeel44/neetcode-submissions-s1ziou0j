"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            nxt = nodes.get(curr.next)
            rnd = nodes.get(curr.random)
            nodes[curr].next = nxt
            nodes[curr].random = rnd
            curr = curr.next
        return nodes.get(head)       
        

        