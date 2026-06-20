class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapList = defaultdict(int)

        for num in nums :
            mapList[num] += 1

        return [key for key, val in mapList.items() if val > len(nums)//3] 
        