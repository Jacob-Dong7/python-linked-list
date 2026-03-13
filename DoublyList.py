class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    
    def add_front(self, value):
        new_node = Node(value)

        if self.head is not None:
            current = self.head
            new_node.set_next(current)
            current.set_prev(new_node)
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.add_length()

    def add_back(self, value):
        new_node = Node(value)

        if self.head is None:
            self.add_front(value)
        else:
            current = self.head
            while current is not None:
                if current.get_next() is None:
                    current.set_next(new_node)
                    new_node.set_prev(current)
                    self.tail = new_node
                    self.add_length()
                    return
                else:
                    current = current.get_next()


    def add_length(self):
        self.length += 1

class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value
        
    def set_next(self, node):
        self.next = node
    
    def set_prev(self, node):
        self.prev = node
    
    def get_next(self):
        return self.next
    

    