class Node:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.left = None    # Pointer to the left child
        self.right = None   # Pointer to the right child

class BinaryTree:
    def __init__(self):
        self.root = None  # Initialize the tree with no root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  # If the tree is empty, the new node becomes the root
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # Insert as the left child
            else:
                self._insert(node.left, value)  # Recursively insert into the left subtree
        else:
            if node.right is None:
                node.right = Node(value)  # Insert as the right child
            else:
                self._insert(node.right, value)  # Recursively insert into the right subtree

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)  # Traverse the left subtree
            print(node.value, end=' ')  # Visit the root
            self.inorder_traversal(node.right)  # Traverse the right subtree

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')  # Visit the root
            self.preorder_traversal(node.left)  # Traverse the left subtree
            self.preorder_traversal(node.right)  # Traverse the right subtree

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)  # Traverse the left subtree
            self.postorder_traversal(node.right)  # Traverse the right subtree
            print(node.value, end=' ')  # Visit the root

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node  # Return the node if found, or None if not found
        if value < node.value:
            return self._search(node.left, value)  # Recursively search in the left subtree
        else:
            return self._search(node.right, value)  # Recursively search in the right subtree

    def delete_tree(self):
        self.root = None  # Simply remove the reference to the root node to delete the tree

# Example usage
if __name__ == "__main__":
    bt = BinaryTree()

    # Insert values into the binary tree
    values_to_insert = [20, 10, 30, 5, 15, 25, 35]
    for value in values_to_insert:
        bt.insert(value)

    # Perform traversals
    print("In-order Traversal:")
    bt.inorder_traversal(bt.root)
    print()

    print("Pre-order Traversal:")
    bt.preorder_traversal(bt.root)
    print()

    print("Post-order Traversal:")
    bt.postorder_traversal(bt.root)
    print()

    # Search for a value
    search_value = 15
    result = bt.search(search_value)
    if result:
        print(f"\nValue {search_value} found in the binary tree.")
    else:
        print(f"\nValue {search_value} not found in the binary tree.")

    # Delete the entire tree
    print("\nDeleting the entire tree...")
    bt.delete_tree()

    # Try to traverse the tree after deletion
    print("In-order Traversal after deleting the tree:")
    bt.inorder_traversal(bt.root)  # Should not print anything since the tree is deleted
    print()
