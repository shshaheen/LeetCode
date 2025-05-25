# Level Order Traversal of a Binary Tree
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        q =deque()
        q.append(root)
        res =[]
        while(q):
            level =[]
            for _ in range(len(q)):
                node = q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                level.append(node.val)
            res.append(level)
        return res
    

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print("Level order traversal of the binary tree is:")
    print(solution.levelOrder(root))
# Output: [[1], [2, 3], [4, 5]]
# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(n) for the queue used in the traversal