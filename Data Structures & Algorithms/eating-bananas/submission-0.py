from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search the range of values k can be (1, max(piles))
        # if not done in time, move l
        # if done in time, record value, move r?
        l, r = 1, max(piles)
        best = None 
        while l <= r:
            m = (l + r) // 2
            # check if its valid
            hours = sum([ceil(x / m) for x in piles])
            if hours > h: 
                l = m + 1
            elif hours <= h:
                best = m
                r = m - 1
        return best
        1234


