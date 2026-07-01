class TrieNode :
    def __init__(self,wordEnd,children) :
        self.wordEnd = wordEnd
        self.children = children
    
    def getChildren(self,char: String) :
        try :
            return self.children[char]
        except :
            return None
    
    def getEnd(self) :
        return self.wordEnd
    
    def modifyValues(self,wordEnd,newChild) :
        self.wordEnd = wordEnd
        self.children = self.children | newChild

class PrefixTree:

    def __init__(self):
        self.rootNode = TrieNode("#",{})

    def insert(self, word: str) -> None:
        currentNode = self.rootNode
        for char in list(word) :
            if currentNode.getChildren(char) is None:
                newNode = TrieNode(False,{})
                currentNode.modifyValues(currentNode.getEnd(),{char : newNode})
            currentNode = currentNode.getChildren(char)
        currentNode.modifyValues(True,{})


    def search(self, word: str) -> bool:
        currentNode = self.rootNode

        for char in list(word) :
            if currentNode.getChildren(char) is None:
                return False
            currentNode = currentNode.getChildren(char)
        return currentNode.getEnd()

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.rootNode
        for char in list(prefix) :
            if currentNode.getChildren(char) is None:
                return False
            currentNode = currentNode.getChildren(char)
        return True
        
        