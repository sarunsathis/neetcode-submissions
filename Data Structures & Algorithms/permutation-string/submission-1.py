class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        low = 0

        while low < len(s2) - s1Len + 1:
            if Counter(s2[low : low + s1Len]) == Counter(s1) :
                return True
            low += 1
        
        return False
