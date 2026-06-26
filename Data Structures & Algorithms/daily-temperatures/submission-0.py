class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)) :
            j = i
            while j < len(temperatures) :
                if temperatures[j] > temperatures[i] :
                    result.append(j-i)
                    break
                j += 1
            result.append(0) if j == len(temperatures) else ""
        return result