class Solution:
    def dfs(self,i: int, total: int, nums: List[int], target: int) :
        if (total > target) or (len(nums) <= i) :
            return
        elif (total == target) :
            self.res.append(self.sumSet.copy())
            return

        self.sumSet.append(nums[i])
        total += nums[i]
        self.dfs(i,total,nums,target)
        total -= self.sumSet.pop()

        if i + 1 >= len(nums) :
            return

        self.dfs(i+1,total,nums,target)
            
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.sumSet = []

        self.dfs(0,0,nums,target)
        return self.res
