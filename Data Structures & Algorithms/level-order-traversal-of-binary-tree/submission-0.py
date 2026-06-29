# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = [root]

        while len(stack) :
            newStack = []
            subList = []
            while len(stack) :
                node = stack.pop(0)
                if node is not None:
                    subList.append(node.val)
                    newStack.append(node.left)
                    newStack.append(node.right)
                    
            stack = newStack
            if len(subList) :
                res.append(subList)

        return res
