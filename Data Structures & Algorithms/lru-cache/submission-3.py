class LRUCache:
    class ListNode:
        def __init__(self, key=0, val=0, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.mp = {}
        self.cap = capacity
        self.head = self.ListNode()
        self.tail = self.ListNode(0, None, self.head)
        self.head.next = self.tail
        

    def get(self, key: int) -> int:
        node = self.mp.get(key)
        if node:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            first = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = first
            first.prev = node
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            prev, next = node.prev, node.next
            prev.next = next
            next.prev = prev
        elif len(self.mp) >= self.cap:
            last = self.tail.prev
            self.tail.prev = last.prev
            last.prev.next = self.tail
            self.mp.pop(last.key, None)
        first = self.head.next
        newNode = self.ListNode(key, value, first, self.head)
        self.head.next = newNode
        first.prev = newNode
        self.mp[key] = newNode
        return None


        # cap 2 -> null
        # 1 -> null
        # 2, 1 -> null
        # 1, 2 -> 1
        # 3, 1 -> null
        # 3, 1 -> -1
        # 4, 3 -> null
        # 4, 3 -> -1
        # 3, 4 -> 3
        # 4, 3 -> 4



        
