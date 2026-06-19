class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        for i in nums :
            result[i] += 1
        return [i for i, v in sorted(result.items(), key=lambda item: item[1], reverse=True)[:k]]