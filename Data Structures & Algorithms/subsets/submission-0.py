class Solution:
    subset = []
    res = []

    def dfs(self, i: int,  nums: List[int]) : 
        if len(nums) <= i :
            self.res.append(self.subset.copy())
            return
        
        self.subset.append(nums[i])
        self.dfs(i+1,nums)

        self.subset.pop()
        self.dfs(i+1,nums)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        self.res = []

        self.dfs(0,nums)
        return self.res