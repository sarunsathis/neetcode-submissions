class Solution:
    def backTrack(self, index: int, total: int, candidates: List[int], target:int) :
        if total == target :
            self.sumSet.append(self.currSubSet.copy())
            return
        elif total > target or index >= len(candidates) :
            return

        self.currSubSet.append(candidates[index])
        total += candidates[index]
        self.backTrack(index+1,total,candidates,target)

        total -= self.currSubSet.pop()
        while index < len(candidates)-1 and candidates[index] == candidates[index+1] :
            index += 1
        self.backTrack(index+1,total,candidates,target)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.currSubSet = []
        self.sumSet = []
        candidates.sort()

        self.backTrack(0,0,candidates,target)
        return self.sumSet
        