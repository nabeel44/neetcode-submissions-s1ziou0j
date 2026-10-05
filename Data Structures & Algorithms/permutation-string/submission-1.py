class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        res = defaultdict(int)
        for c in s1:
            freq[c] += 1
        l = 0
        for r in range(len(s2)):
            if sum(res.values()) < len(s1):
                res[s2[r]] += 1
            elif res != freq:
                res[s2[l]] -= 1
                if res[s2[l]] == 0:
                    res.pop(s2[l])
                res[s2[r]] += 1
                l += 1
            else:
                return True
        return res == freq




        