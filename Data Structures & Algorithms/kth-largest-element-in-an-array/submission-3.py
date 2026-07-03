class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numList = [x * (-1) for x in nums]
        heapq.heapify(numList)
        for ind in range(k-1) :
            heapq.heappop(numList)

        return heapq.heappop(numList) * (-1)