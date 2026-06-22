class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        strList = [x for x in s if x.isalpha() or x.isdigit()]
        for i in range(len(strList)//2) :
            if strList[i] != strList[-1 - i] :
                return False
        return True
        