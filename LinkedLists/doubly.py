class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the end of the list
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        if self.head is None:  # If the list is empty
            return
        current = self.head
        while current:
            if current.data == key:
                if current.prev:  # Not the head node
                    current.prev.next = current.next
                else:  # Deleting the head node
                    self.head = current.next
                if current.next:  # If there is a node after the current node
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print("Doubly Linked List:", " <-> ".join(map(str, nodes)))

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.display()  # Output: Doubly Linked List: 0 <-> 1 <-> 2 <-> 3

dll.delete_node(2)
dll.display()  # Output: Doubly Linked List: 0 <-> 1 <-> 3
