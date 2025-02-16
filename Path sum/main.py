class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root:TreeNode, targetSum:int)->bool:
    if not root:
        return False

    targetSum -= root.val

    if not root.left and not root.right:
        return targetSum == 0

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

targetSum = 22

# Input: root = [
    # 5,4,
    # 8,11,
    # null,13,
    # 4,7,
    # 2,null,
    # null,null,
    # 1
    # ], targetSum = 22

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(hasPathSum(root, 18))  # Output: True
print(hasPathSum(root,targetSum))