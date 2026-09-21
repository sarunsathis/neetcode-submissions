class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        
        for idx in range(n - 2) :
            if nums[idx] > 0 :
                break
            elif idx > 0 and nums[idx] == nums[idx - 1] :
                continue
            
            low = idx + 1
            high = n - 1
            currVal = nums[idx]
            while low < high :
                total = nums[low] + nums[high] + currVal

                if total < 0 :
                    low += 1
                elif total > 0 :
                    high -= 1
                else :
                    res.append([currVal,nums[low],nums[high]])
                    high -= 1
                    low += 1
                    while low < high and nums[low] == nums[low - 1] :
                        low += 1
                    while low < high and nums[high] == nums[high + 1] :
                        high -= 1
        
        return res