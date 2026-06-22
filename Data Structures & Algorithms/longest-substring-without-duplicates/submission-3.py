class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        maxLen = i = 1
        text = list(s)
        while i < len(text) :
            if text[i] not in text[low:i] :
                maxLen = max(maxLen,len(text[low:i+1]))
            elif low < i :
                low += 1
                continue 
            i += 1
        return maxLen if s != "" else 0