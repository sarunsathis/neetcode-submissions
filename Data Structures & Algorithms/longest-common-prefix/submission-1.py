class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longVal = strs[0]
        for i in range(1,len(strs)) :
            word = strs[i]
            for j in range(len(longVal)):
                try:
                    if longVal[j] != word[j] :
                        longVal = longVal[:j]
                        break
                except IndexError as error:
                    longVal = longVal[:j]
                    break
        return longVal