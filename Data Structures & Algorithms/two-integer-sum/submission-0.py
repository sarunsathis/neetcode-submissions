class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapVal = {}
        for i in range(len(nums)) :
            expected_val = target - nums[i]
            if mapVal.get(nums[i]) == None :
                mapVal[expected_val] = i
                print(expected_val)
                print(mapVal)
            else :
                return [mapVal[nums[i]],i]
        return [0,0]