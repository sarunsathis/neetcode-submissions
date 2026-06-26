class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ["(","{","["] :
                stack.append(x)
            else :
                if len(stack) == 0 : return False
                if stack[-1] == ["(","{","["][[")","}","]"].index(x)] :
                    stack = stack[:-1]
                else :
                    return False
        
        return True if len(stack) == 0 else False
        