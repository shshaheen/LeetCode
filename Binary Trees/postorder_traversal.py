# post-order traversal of a binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')
# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Postorder traversal of the binary tree is:")
    postorder_traversal(root)  # Output: 4 5 2 3 1
# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree (due to recursion stack)