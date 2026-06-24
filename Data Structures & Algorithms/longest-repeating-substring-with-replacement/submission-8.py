class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxLen = 0
        r = 1
        

        while r <= len(s) :
            window = s[l:r]
            mostCommonCount = Counter(window).most_common(1)[0][1]
            if (len(window) - mostCommonCount) <= k :
                maxLen = max(maxLen,len(window))
                r += 1
            else :
                l += 1
        
        return maxLen

