class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        while j < len(nums) :
            ele = nums[j]
            if ele == val :
                nums.pop(j)
                continue
            j += 1
        print(nums)
        return len(nums)        