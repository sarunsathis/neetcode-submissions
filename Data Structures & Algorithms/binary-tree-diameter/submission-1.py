# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDiameter = 0

    def maxDepth(self,root: Optional[TreeNode]) -> int :
        if root is None : return 0
        leftDepth = rightDepth = 0

        if root.right is None and root.left is None :
            return 1

        if root.left is not None :
            leftDepth = self.maxDepth(root.left) + 1
        if root.right is not None :
            rightDepth = self.maxDepth(root.right) + 1
        

        self.maxDiameter = max(self.maxDiameter,leftDepth + rightDepth - 2)
        return max(leftDepth,rightDepth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None : return 0
        if root.left is None and root.right is None : return 0

        leftDepth = rightDepth = 0

        if root.left is not None :
            leftDepth = self.maxDepth(root.left)
        if root.right is not None :
            rightDepth = self.maxDepth(root.right)

        print(leftDepth,rightDepth)
        return max(self.maxDiameter,leftDepth + rightDepth)

