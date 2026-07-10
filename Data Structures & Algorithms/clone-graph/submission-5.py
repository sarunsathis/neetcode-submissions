"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    visitedMap = {}

    def deepCopyNode(self, node: Optional['Node']) -> Optional['Node']:
        if node.val in self.visitedMap.keys() :
            return self.visitedMap[node.val]

        newNode = Node(node.val)
        self.visitedMap[node.val] = newNode
        neighborlist = []

        for nodes in node.neighbors :
            neighborlist.append(self.deepCopyNode(nodes))

        newNode.neighbors = neighborlist
        return newNode


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visitedMap = {}
        if node is None : 
            return None
        
        return self.deepCopyNode(node)
        