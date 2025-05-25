# Inorder Traversal of a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)
# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal of the binary tree is:")
    inorder_traversal(root)  # Output: 4 2 5 1 3
#Time Complexity: O(n) where n is the number of nodes in the tree
#Space Complexity: O(h) where h is the height of the tree (due to recursion stack)