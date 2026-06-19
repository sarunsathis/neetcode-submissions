class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while len(strs) > 0 :
            word = strs[0]
            sublist = [word]
            strs.pop(0)
            j = 0
            while j < len(strs) :
                try :
                    currentWord = strs[j]
                    if len(currentWord) == len(word):
                        if Counter(currentWord) == Counter(word) :
                            sublist.append(currentWord)
                            strs.pop(j)
                            j -= 1
                    j += 1
                except IndexError:
                    break
            result.append(sublist)

        return result
        