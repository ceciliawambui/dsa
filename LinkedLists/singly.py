class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:  # If the node to delete is the head
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:  # If the key was not found
            return
        prev.next = current.next
        current = None

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The previous node must be in the LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print("Singly Linked List:", " -> ".join(map(str, nodes)))

# Example usage
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.prepend(0)
sll.display()  # Output: Singly Linked List: 0 -> 1 -> 2 -> 3

sll.delete_node(2)
sll.display()  # Output: Singly Linked List: 0 -> 1 -> 3

sll.insert_after_node(sll.head.next, 5)
sll.display()  # Output: Singly Linked List: 0 -> 1 -> 5 -> 3
