class DoubleList:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise
        self.capacity = capacity
        self.d = {}
        self.head = DoubleList()
        self.tail = DoubleList()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_to_the_head(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def get(self, key: int) -> int:
        # 如果不在Cache中就返回-1
        if key not in self.d:
            return -1
        # 如果在就取出并将节点更新到头结点
        node = self.d[key]
        self.move_to_the_head(node)
        return self.head.next.val

    def put(self, key: int, value: int) -> None:
        # 如果key已经在Cache中就更新到头结点
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.move_to_the_head(node)
        # 如果key不在Cache中
        else:
            node = DoubleList(key, value)
            # 如果链表已满删除末尾节点
            if len(self.d) >= self.capacity:
                last = self.tail.pre
                last.next.pre = last.pre
                last.pre.next = last.next
                del_key = last.key
                del self.d[del_key]
                del last
            # 插入头结点
            node.next = self.head.next
            self.head.next.pre = node
            node.pre = self.head
            self.head.next = node
            self.d[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)