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
            print("--------------------------")
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

    def delete_by_value(self, value):
        value_change = int(value)

        current = self.head
        previous = current
        i = 1

        while current is not None:
    
            if int(current.get_value()) == value_change:
                if i == 1:
                    self.delete_head()
                elif current.get_next() == None:
                    previous.set_next(None)
                    self.length -= 1
                else:
                    previous.set_next(current.get_next())
                    self.length -= 1
                return
            else:
                previous = current
                current = current.get_next()
                i += 1


    """A B C"""
    def delete_by_index(self, value):
        index = int(value)

        if index > self.length or index <= 0:
            print("--------------------------")
            print("Index out of bound")
        if index == 1:
            self.delete_head()
            return
    
        current = self.head
        previous = current
        i = 1
        while True:
            if i == index:
                previous.set_next(current.get_next())
                self.length -= 1
                return
            else:
                previous = current
                current = current.get_next()
                i += 1
    
    def delete_head(self):
        current = self.head
        next = current.get_next()
        self.head = next
        self.length -= 1



        
        
    
    def set_new(self, new_node):
        new_node.set_next(self.head)
        self.head = new_node

    def print(self):
        current = self.head
        if self.length <= 0:
            print("Empty")
            return
        while current is not None:
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
