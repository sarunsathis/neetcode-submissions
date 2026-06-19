class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0 for i in range(2 * len(nums))]
        for i in range(0,len(nums)):
            arr[i] = nums[i]
            arr[i+len(nums)] = nums[i]

        return arr
        