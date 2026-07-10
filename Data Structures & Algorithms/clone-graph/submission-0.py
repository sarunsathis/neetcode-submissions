"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def copyNodes(self, node : Optional['Node']):
        if node.val in self.visitedMap.keys() :
            return self.visitedMap[node.val]

        newNode = Node(node.val,node.neighbors)
        self.visitedMap[node.val] = newNode
        neighborlist = []

        for nodes in node.neighbors :
            neighborlist.append(self.copyNodes(nodes))

        node.neighbors = neighborlist
        return newNode

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None : 
            return None
        
        self.visitedMap = {}
        newRootNode = Node(node.val,[])
        self.visitedMap[node.val] = newRootNode
        neighborlist = []
        
        for nodes in node.neighbors :
            neighborlist.append(self.copyNodes(nodes))

        newRootNode.neighbors = neighborlist
        return newRootNode