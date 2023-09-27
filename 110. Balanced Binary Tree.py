# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Helper function to calculate the height of a subtree
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            
            # If the subtree is not balanced (-1 means it's not balanced)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the balanced subtree
            return max(left_height, right_height) + 1
        
        # Start the recursion from the root
        return height(root) != -1
