class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eleCount = Counter(nums)
        listHeap = []
        for key,value in eleCount.items() :
            heapq.heappush(listHeap,[value * (-1),key]) 

        return [heapq.heappop(listHeap)[-1] for _ in range(k)]