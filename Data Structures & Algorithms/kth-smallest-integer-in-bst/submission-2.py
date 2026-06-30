# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSmallestk(self,root: Optional[TreeNode],k: int, count: int, finalVal: int) -> List :
        if k == count :
            return [count,finalVal]
        if root is None:
            return [count,finalVal]
        
        count, finalVal = self.findSmallestk(root.left,k,count,finalVal)
        if k != count :
            count += 1
            finalVal = root.val
        count, finalVal = self.findSmallestk(root.right,k,count,finalVal)
        
        return [count,finalVal]
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count,val = self.findSmallestk(root.left,k,0,0)

        if k != count :
            count += 1
            val = root.val
        count,val = self.findSmallestk(root.right,k,count,val)
        return val
        