from Node import Node
class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_tail(self, data):
        node = Node(data)
        if self.tail is None:  # lista vacía
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) + " -> None"
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def _node_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("índice fuera de rango")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur  
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pop_first(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    def pop(self):  # eliminar cola
        if self.is_empty():
            raise IndexError("lista vacía")
        if self._size == 1:
            return self.pop_first()
        prev = self._node_at(self._size - 2)
        data = prev.next.data
        prev.next = None
        self.tail = prev
        self._size -= 1
        return data
    
    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def find(self, target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def ordenar(self, data)
    
sll = SinglyLinkedList()
sll.append_tail(1)
sll.append_tail(1)
sll.append_tail(3)
sll.append_tail(4)
sll.append_tail(5)
        
#sll.append(8)

#sll.pop_first()

print(sll)

#print(sll.find_mod(1))

