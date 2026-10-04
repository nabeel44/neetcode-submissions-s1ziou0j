class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freq = defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(freq.values())
            if maxFreq + k < r - l + 1:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


