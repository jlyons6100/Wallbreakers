class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.map = {} # key, (value, pointer) to node
        self.cap = capacity
        self.size = 0
        self.head = None
        self.tail = None
    def get(self, key: int) -> int:
        if not key in self.map:
            return -1
        val = self.map[key][0] # value
        #update priority
        key_node = self.map[key][1]
        print("key_node:" + str(key_node.key))
        if key_node.prev != None:
            print(key_node.prev.key)
        if key_node.next != None:
            print(key_node.next.key)
        if key_node.prev == None and key_node.next != None:
            nextt = key_node.next
            nextt.prev = None
            self.head.next = key_node
            key_node.next = None
            key_node.prev = self.head
            self.head = key_node
            self.tail = nextt
        elif key_node == self.head:
            pass
        elif key_node.prev != None and key_node.next != None:
            nextt = key_node.next
            prevv = key_node.prev
            prevv.next = nextt
            nextt.prev = prevv
            key_node.next = None
            key_node.prev = self.head
            self.head.next = key_node
            self.head = key_node
        return val
    def put(self, key: int, value: int) -> None:
        if self.size < self.cap:
            if self.size == 0:
                n = Node(key)
                self.head = n
                self.tail = n
                self.map[key] = (value, n)
                self.size += 1
            else:
                if key not in self.map:
                    n = Node(key)
                    self.head.next = n
                    n.prev = self.head
                    self.head = n
                    self.map[key] = (value, n) 
                    self.size += 1
                else:
                    node = self.map[key][1]
                    if node.prev == None and node.next != None:
                        nextt = node.next
                        nextt.prev = None
                        self.tail = nextt
                        node.next = None
                        node.prev = self.head
                        self.head.next = node
                        self.head = node
                    elif node == self.head:
                        pass
                    elif node.prev != None and node.next != None:
                        nextt = node.next
                        prevv = node.prev
                        prevv.next = nextt
                        nextt.prev = prevv
                        node.next = None
                        node.prev = self.head
                        self.head.next = node
                        self.head = node
                    self.map[key] = (value, node)
            
        else:
            if self.tail == self.head and self.cap == 1:
                node = Node(key)
                del self.map[self.tail.key]
                self.tail = node
                self.head = node
                self.map[key] = (value, node)
                return
            if key in self.map:
                node = self.map[key][1]
                if node.prev == None and node.next != None:
                    nextt = node.next
                    nextt.prev = None
                    node.next = None
                    self.tail = nextt
                    node.prev = self.head
                    self.head.next = node
                    self.head = node
                elif node == self.head:
                    pass
                elif node.prev != None and node.next != None:
                    nextt = node.next
                    prevv = node.prev
                    prevv.next = nextt
                    nextt.prev = prevv
                    node.next = None
                    node.prev = self.head
                    self.head.next = node
                    self.head = node
                self.map[key] = (value, node)
                return
            tail = self.tail
            
            nextt = tail.next
            
            nextt.prev = None
            self.tail = nextt
            del self.map[tail.key]
            node = Node(key)
            self.head.next = node
            node.prev = self.head
            self.head = node
            self.map[key] = (value, node)
            cur = self.tail