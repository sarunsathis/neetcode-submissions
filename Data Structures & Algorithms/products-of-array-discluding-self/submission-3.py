class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount,product = 0,1
        for ele in nums :
            if ele :
                product = product * ele
            else :
                zeroCount += 1
        
        if zeroCount > 1 :
            return [0 for i in range(len(nums))]
        elif zeroCount == 1 :
            return [0 if ele != 0 else product for ele in nums]
        else :
            return [product//ele for ele in nums]

        
        