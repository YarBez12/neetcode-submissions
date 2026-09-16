class LRUCache:

    class Item:
        def __init__(self, key, val, prev = None, next = None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.items = {}
        

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        item = self.items[key]
        if item != self.tail:
            if item == self.head:
                self.head = item.next
            if item.prev:
                item.prev.next = item.next
            item.next.prev = item.prev
            self.tail.next = item
            item.next = None
            item.prev = self.tail
            self.tail = item
        return self.items[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items[key].val = value
            self.get(key)
            return
        if self.size == self.capacity:
            del self.items[self.head.key]
            self.head = self.head.next
            if self.capacity == 1:
                self.tail = None
            self.size -= 1
        newItem = self.Item(key, value, self.tail)
        self.items[key] = newItem
        if not self.head:
            self.head = newItem
        if not self.tail:
            self.tail = newItem
        else:
            self.tail.next = newItem
            self.tail = newItem
        self.size += 1

        
