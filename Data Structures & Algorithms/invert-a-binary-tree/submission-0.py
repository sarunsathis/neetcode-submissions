# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None : return root
        root.left,root.right = root.right,root.left

        self.invertTree(root.left) if root.left != None else ""
        self.invertTree(root.right) if root.right != None else ""

        return root