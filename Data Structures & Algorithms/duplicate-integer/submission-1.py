class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set(nums)
        return len(uniqueSet) != len(nums)
        

        