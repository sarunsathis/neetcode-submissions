class Solution:
    def reverseString(self, s: List[str]) -> None:
        for x in range(len(s)//2) :
            s[x],s[len(s) -1 -x] = s[len(s) -1 -x],s[x]
        