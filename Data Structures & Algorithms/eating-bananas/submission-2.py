class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)

        if n == h :
            return piles[-1]

        lowSecond = 0
        low = 0
        high = piles[n-1]

        while low < high and low != (low + high) // 2 :
            rate = (low + high) // 2
            usedHours = 0

            for val in piles :
                usedHours += 1 if val <= rate else (val//rate + (1 if val%rate != 0 else 0))

            if usedHours > h :
                low = rate
            else :
                lowSecond = rate
                high = rate
        
        return lowSecond

                
