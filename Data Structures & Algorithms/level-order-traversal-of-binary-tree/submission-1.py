# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([[root]])
        res = []

        print(type(dq))

        while len(dq) :
            subList = []
            childNodeList = []
            nodeList = dq.popleft()
            for node in nodeList :
                if node is not None :
                    subList.append(node.val)
                    childNodeList.append(node.left)
                    childNodeList.append(node.right)

            if len(childNodeList) > 0 :
                res.append(subList)
                dq.append(childNodeList)

        return res

        