class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxLen = 0
        r = 1
        
        while r <= len(s) :
            mostCommonCount = Counter(s[l:r]).most_common(1)[0][1]
            if (len(s[l:r]) - mostCommonCount) <= k :
                maxLen = max(maxLen,len(s[l:r]))
                r += 1
            else :
                l += 1
        
        return maxLen

