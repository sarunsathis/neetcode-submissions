class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        maxLen = 0
        while i < len(nums) :
            current = nums[i]
            subLen = 1
            while True :
                if current + 1 in nums :
                    subLen += 1
                    current += 1
                    nums.remove(current)
                else :
                    break
            
            current = nums[i]
            while True :
                if current - 1 in nums :
                    subLen += 1
                    current -= 1
                    nums.remove(current)
                else :
                    break
            maxLen = max(maxLen,subLen)
            i += 1
        
        return maxLen