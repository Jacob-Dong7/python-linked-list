class linked_list:

    def __init__(self):
        self.head = None
        self.length = 0
    
    def get_length(self):
        return self.length
    
    def add_front(self, value):
        new_node = Node(value)

        """if head does not exist, set new_node as the new head, else add it to the front"""
        if not self.head:
            self.head = new_node
        else:
            self.set_new(new_node)
        
        self.length += 1

    def add_tail(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            self.find_tail(new_node)

        self.length += 1

    def find_tail(self, new_node):
        current = self.head
        while True:
            if current.get_next() != None:
                current = current.get_next()
            else:
                current.set_next(new_node)
                new_node.set_next(None)
                return
            
    def add_at(self, value, index):
        new_index = int(index)
        new_node = Node(value)

        if new_index == 1:
            self.set_new(new_node)
            return
        
        if new_index > self.length or new_index <= 0:
            print("Index out of bound")
            return
        else:
            i = 1
            current = self.head
            previous = current
            while True:

                if i == new_index:
                    previous.set_next(new_node)
                    new_node.set_next(current)
                    self.length += 1
                    return
                else:
                    previous = current
                    current = current.get_next()
                    i += 1  
                    continue            
        
    
    def set_new(self, new_node):
        new_node.set_next(self.head)
        self.head = new_node

    def print(self):
        current = self.head
        if self.length <= 0:
            print("Empty")
            return
        while True:
            if current.get_next() != None:
                print(current.get_value(),end=" -> ")
                current = current.get_next()
            else:
                print(current.get_value())
                return
    



class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
