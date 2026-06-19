class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        for ele in nums :
            if countMap[ele] + 1 > len(nums)//2:
                return ele
            else :
                countMap[ele] += 1
                
        