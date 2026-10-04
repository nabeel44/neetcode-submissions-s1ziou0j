class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: 
            return len(s)
        charSet = set()
        l, r = 0, 1
        length = 0
        while r < len(s):
            charSet.add(s[l])
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = max(length, r-l+1)
            r += 1
        return length



                
