class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left) 
        print(node.data, end=' ')     
        inorder_traversal(node.right) 

def preorder_traversal(node):
    if node:
        print(node.data, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=' ')

first_tree = Node(20)
first_tree.left = Node(40)
first_tree.left.left = Node(30)
first_tree.left.right = Node(25)
first_tree.right = Node(10)
first_tree.right.left = Node(5)
first_tree.right.right = Node(15)

print("In-order Traversal:")
inorder_traversal(first_tree)
print("\nPre-order Traversal:")
preorder_traversal(first_tree)
print("\nPost-order Traversal:")
postorder_traversal(first_tree)






