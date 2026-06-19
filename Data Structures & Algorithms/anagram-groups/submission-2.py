class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while len(strs) > 0 :
            word = strs[0]
            sublist = [word]
            word = list(word)
            word.sort()
            strs.pop(0)
            j = 0
            while j < len(strs) :
                try :
                    currentWord = list(strs[j])
                    currentWord.sort()
                    if len(currentWord) == len(word):
                        if currentWord == word :
                            sublist.append(strs[j])
                            strs.pop(j)
                            j -= 1
                    j += 1
                except IndexError:
                    break
            result.append(sublist)
        print(result)
        return result
        