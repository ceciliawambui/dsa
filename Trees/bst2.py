class Node:
    def __init__(self, value):
        self.value = value  # Value of the node
        self.left = None    # Left child of the node
        self.right = None   # Right child of the node

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  # If the tree is empty, the value becomes the root
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

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node  # Return the node if found, or None if not found
        if value < node.value:
            return self._search(node.left, value)  # Recursively search in the left subtree
        else:
            return self._search(node.right, value)  # Recursively search in the right subtree

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._min_value_node(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert values into the BST
    values_to_insert = [20, 40, 30, 25, 10, 5, 15]
    for value in values_to_insert:
        bst.insert(value)

    # Perform traversals
    print("In-order Traversal:")
    bst.inorder_traversal(bst.root)
    print()

    print("Pre-order Traversal:")
    bst.preorder_traversal(bst.root)
    print()

    print("Post-order Traversal:")
    bst.postorder_traversal(bst.root)
    print()

    # Search for a value
    search_value = 25
    result = bst.search(search_value)
    if result:
        print(f"\nValue {search_value} found in the BST.")
    else:
        print(f"\nValue {search_value} not found in the BST.")

    # Delete a value
    delete_value = 40
    print(f"\nDeleting value {delete_value} from the BST.")
    bst.delete(delete_value)

    # In-order traversal after deletion
    print("In-order Traversal after deletion:")
    bst.inorder_traversal(bst.root)
    print()
