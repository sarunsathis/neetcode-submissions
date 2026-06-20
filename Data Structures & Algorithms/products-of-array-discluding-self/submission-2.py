class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        leftProduct = 1
        
        for i in range(0,len(nums)) :
            product = leftProduct
            for j in range(i+1,len(nums)) :
                product = product * nums[j]
            result.append(product)
            leftProduct = leftProduct * nums[i]
        return result
        
        