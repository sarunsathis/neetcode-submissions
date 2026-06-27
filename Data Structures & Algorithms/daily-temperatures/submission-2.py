class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        i = len(temperatures) - 1

        while i > 0 :
            i -= 1
            if temperatures[i] < temperatures[i+1] :
                res[i] = 1
            elif temperatures[i] >= temperatures[i+1] :
                if res[i+1] == 0 :
                    continue
                j = res[i+1] + i + 1
                while j < len(temperatures) :
                    if temperatures[j] > temperatures[i] :
                        res[i] = j - i
                        break
                    elif temperatures[j] <= temperatures[i] :
                        if res[j] == 0 :
                            break
                        j = res[j] + j
        return res

        
