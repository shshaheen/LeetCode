# Pre-Order Traversal of a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def preorder_traversal(root):
    if root is not None:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)
# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal of the binary tree is:")
    preorder_traversal(root)  # Output: 1 2 4 5 3

# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree (due to recursion stack)