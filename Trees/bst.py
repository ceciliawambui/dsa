class Node:
    def __init__(self, value):
        self.value = value  # The value of the node
        self.left = None    # Pointer to the left child
        self.right = None   # Pointer to the right child

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the tree with no root

    def insert(self, value):
        """Insert a new value into the BST."""
        if self.root is None:
            self.root = Node(value)  # If the tree is empty, create the root
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """Helper method to insert a new value recursively."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # Insert as the left child
            else:
                self._insert(node.left, value)  # Recur to the left subtree
        else:
            if node.right is None:
                node.right = Node(value)  # Insert as the right child
            else:
                self._insert(node.right, value)  # Recur to the right subtree

    def search(self, value):
        """Search for a value in the BST."""
        return self._search(self.root, value)

    def _search(self, node, value):
        """Helper method to search for a value recursively."""
        if node is None:
            return False  # The value is not found
        if value == node.value:
            return True  # The value is found
        elif value < node.value:
            return self._search(node.left, value)  # Search in the left subtree
        else:
            return self._search(node.right, value)  # Search in the right subtree

    def inorder_traversal(self, node):
        """Perform in-order traversal (left, root, right)."""
        if node:
            self.inorder_traversal(node.left)  # Traverse the left subtree
            print(node.value, end=' ')  # Print the node's value
            self.inorder_traversal(node.right)  # Traverse the right subtree

    def preorder_traversal(self, node):
        """Perform pre-order traversal (root, left, right)."""
        if node:
            print(node.value, end=' ')  # Print the node's value
            self.preorder_traversal(node.left)  # Traverse the left subtree
            self.preorder_traversal(node.right)  # Traverse the right subtree

    def postorder_traversal(self, node):
        """Perform post-order traversal (left, right, root)."""
        if node:
            self.postorder_traversal(node.left)  # Traverse the left subtree
            self.postorder_traversal(node.right)  # Traverse the right subtree
            print(node.value, end=' ')  # Print the node's value

# Create a Binary Search Tree
bst = BinarySearchTree()

# Insert values into the tree
values_to_insert = [20, 40, 30, 25, 10, 5, 15]
for value in values_to_insert:
    bst.insert(value)

# Search for a value in the tree
search_value = 25
found = bst.search(search_value)
print(f"Value {search_value} found in BST: {found}")

# Perform and print traversals
print("In-order Traversal:")
bst.inorder_traversal(bst.root)
print()

print("Pre-order Traversal:")
bst.preorder_traversal(bst.root)
print()

print("Post-order Traversal:")
bst.postorder_traversal(bst.root)
print()
