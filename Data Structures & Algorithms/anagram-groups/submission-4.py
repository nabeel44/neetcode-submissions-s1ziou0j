class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            freq = [0] * 26
            for char in word:
                idx = ord('a') - ord(char)
                freq[idx] += 1
            key = tuple(freq)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())
            
        
        