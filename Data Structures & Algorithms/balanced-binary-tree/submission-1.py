# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def setBalanceFlag(self,balanceFlag : bool) :
        self.balanceFlag = balanceFlag

    def treeHeight(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        leftHeight = self.treeHeight(root.left)
        rightHeight = self.treeHeight(root.right)

        if abs(leftHeight - rightHeight) >= 2 :
            self.setBalanceFlag(False)

        return max(leftHeight,rightHeight) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None : return True

        self.setBalanceFlag(True)
        self.treeHeight(root)

        return self.balanceFlag
        