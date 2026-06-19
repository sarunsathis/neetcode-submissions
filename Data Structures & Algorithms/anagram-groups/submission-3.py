class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for val in strs :
            sortedString = ''.join(sorted(val))
            result[sortedString].append(val)
        return list(result.values())
        