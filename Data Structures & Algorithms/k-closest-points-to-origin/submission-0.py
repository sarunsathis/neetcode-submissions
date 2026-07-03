class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heapList = []
        for point in points :
            heapq.heappush(heapList,[(point[0]**2 + point[1]**2)**0.5, point])

        return [heapq.heappop(heapList)[-1] for _ in range(k)]
        