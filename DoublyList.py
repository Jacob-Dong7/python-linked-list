class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get_length(self):
        return self.length
    
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
    
    def add_at(self, value, user_index):
        index = int(user_index)
        if index > self.length or index <= 0:
            print("Index is out of bound")
            return
        if self.head is None: 
            print("List Empty")
            return
        if index == 1:
            self.add_front(value)
            return
        
        current = self.head
        i = 1
        target = int(index)
        new_node = Node(value)
        
        """a b c-e-d """
        while current is not None:
            if i == target:
                if current.get_next() is None:
                    previous = current
                    previous.set_next(new_node)

                    new_node.set_prev(previous)

                    self.tail = new_node
                else:
                    previous = current
                    next = current.get_next()
                    previous.set_next(new_node)
                    new_node.set_prev(previous)
                    new_node.set_next(next)
                    next.set_prev(new_node)
                
                self.add_length()
                return

            else:
                i += 1
                current = current.get_next()
            
    def print(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            current = self.head
            while current is not None:
                if current.get_next() is None:
                    print(current.get_value())
                    return
                else:
                    print(current.get_value(), end=" -> ")
                    current = current.get_next()
                
    def print_reverse(self):
        if self.tail is None or self.head is None:
            print("List is empty")
            return
        else:
            current = self.tail
            while current is not None:
                if current.get_prev() is None:
                    print(current.get_value())
                    return
                else:
                    print(current.get_value(),end=" -> ")
                    current = current.get_prev()

    def delete_first(self):
        current = self.head
        if current.get_next() is not None:
            next = current.get_next()
            current.set_next(None)
            next.set_prev(None)
            self.head = next
        else:
            self.head = None
            self.tail = None

        
    def delete_by_value(self, value):

        if value is None:
            print("Empty Value")
            return
        value = int(value)
        
        if self.head is None or self.tail is None:
            print("List is empty or incomplete")
            return
        
        current = self.head
        
        while current is not None:
            if int(current.get_value()) == value:
                """if last node a b c"""
                if current.get_prev() is None and current.get_next() is None:
                    self.head = None
                    self.tail = None
                elif current.get_next() is None:
                    previous = current.get_prev()
                    previous.set_next(None)
                    self.tail = previous
                elif current == self.head:
                    self.delete_first()
                else:
                    previous = current.get_prev()
                    next = current.get_next()
                    previous.set_next(next)
                    next.set_prev(previous)
                self.remove_length()
                return
            else:
                current = current.get_next()
        print("Value Not Found")

    def delete_by_index(self, user_index):
        index = int(user_index)

        if index == 1:
            self.delete_first()
            self.remove_length()
            return
        if index > self.length or index <= 0:
            print("Index out of bound")
            return
        
        if self.head is None or self.tail is None:
            print("List is empty or incomplete")
            return
        
        current = self.head
        i = 1
        while current is not None:
            if i == index:
                """If last node a b c"""
                if current.get_next() is None:
                    previous = current.get_prev()
                    previous.set_next(None)
                    self.tail = previous
                else:
                    previous = current.get_prev()
                    next = current.get_next()
                    previous.set_next(next)
                    next.set_prev(previous)
                
                self.remove_length()
                return
            else:
                i += 1
                current = current.get_next()
        
        


        
    def remove_length(self):
        self.length -= 1

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
    
    def get_prev(self):
        return self.prev
    
    def get_value(self):
        return self.value
    

    