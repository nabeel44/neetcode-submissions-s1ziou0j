class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        countS = Counter('')
        l = 0
        have, need = 0, len(countT)
        bestL, bestR = 0, float('inf')

        for r in range(len(s)):
            countS[s[r]] += 1
            if countS[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < bestR - bestL + 1:
                    bestL, bestR = l, r
                countS[s[l]] -= 1
                if countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return '' if bestR == float('inf') else s[bestL:bestR+1]

                


                

