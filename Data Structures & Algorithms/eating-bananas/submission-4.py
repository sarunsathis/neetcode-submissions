class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        if n == h :
            return max(piles)

        low = 1
        high = max(piles)

        while low < high :
            rate = (low + high) // 2
            usedHours = 0

            for val in piles :
                usedHours += 1 if val <= rate else (val//rate + (1 if val%rate != 0 else 0))

            if usedHours > h :
                low = rate + 1
            else :
                high = rate
        
        return low

                
