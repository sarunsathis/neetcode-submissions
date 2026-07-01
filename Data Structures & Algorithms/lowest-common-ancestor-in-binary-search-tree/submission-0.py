# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    nodeFound = {}
    parentNode = {}

    def findParentNode(self, root: TreeNode, searchNode: TreeNode) -> bool :
        if root is None:
            return False
        
        if root.val == searchNode.val :
            self.nodeFound[searchNode.val] = True
        elif root.val > searchNode.val :
            self.findParentNode(root.left,searchNode)
        else :
            self.findParentNode(root.right,searchNode)

        if self.nodeFound[searchNode.val] :
            self.parentNode[searchNode.val].appendleft(root)
            return True

        return True

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.nodeFound[p.val] = False 
        self.nodeFound[q.val] = False
        commonRoot = root
        self.parentNode[p.val] = deque([])
        self.parentNode[q.val] = deque([])


        self.findParentNode(root,p)
        self.findParentNode(root,q)

        

        while self.parentNode[p.val] and self.parentNode[q.val]:
            qroot = self.parentNode[q.val].popleft()
            proot = self.parentNode[p.val].popleft()

            if qroot.val != proot.val :
                return commonRoot
            else :
                commonRoot = qroot
        return commonRoot
