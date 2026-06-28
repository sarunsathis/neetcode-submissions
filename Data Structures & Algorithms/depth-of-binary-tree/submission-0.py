# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxdepth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        leftDepth = rightDepth = 1
        if root == None : return 0
        if root.left == None and root.right == None : return 1

        if root.left != None :
            leftDepth = leftDepth + self.maxDepth(root.left)
        if root.right != None :
            rightDepth =rightDepth + self.maxDepth(root.right)
            
        return max(leftDepth,rightDepth)
        