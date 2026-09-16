class LRUCache:

    class Item:
        def __init__(self, key, val, prev = None, next = None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Item(0,0)
        self.tail = self.Item(0,0, self.head)
        self.head.next = self.tail
        self.items = {}
    
    def remove(self, item):
        item.prev.next = item.next
        item.next.prev = item.prev
        item.next = None
        item.prev = None
    
    def append(self, item):
        self.tail.prev.next = item
        item.prev =  self.tail.prev
        item.next = self.tail
        self.tail.prev = item

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        item = self.items[key]
        self.remove(item)
        self.append(item)
        return item.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items[key].val = value
            self.get(key)
            return
        if len(self.items) == self.capacity:
            del self.items[self.head.next.key]
            self.remove(self.head.next)
        newItem = self.Item(key, value, self.tail)
        self.items[key] = newItem
        self.append(newItem)

        
