class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert_right(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def insert_left(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        else:
            current = Node(x, None)
            current.next = self.first
            self.first = current

    def __str__(self):
        if self.first:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

L = LinkedList()
L.insert_right("A")
L.insert_right("B")
L.insert_left("C")
L.insert_right("D")
print(L)
