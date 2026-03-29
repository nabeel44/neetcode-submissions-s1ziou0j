class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        5#hello5#world
        gather word length until you see #
        once you see # iterate through word length to create word
        append word to res
        repeat        
        """
        res = ''
        for word in strs:
            length = len(word)
            res = res + str(length) + '#' + word
        return res

# 2#we3#say1#:3#yes10#!@#$%^&*()

    def decode(self, s: str) -> List[str]:
        i = 0
        wordLength = ''
        word = ''
        res = []
        while i < len(s):
            while s[i] != '#':
                wordLength += (s[i])
                i += 1
            wordLength = int(wordLength)
            i += 1
            while wordLength > 0:
                word += s[i]
                i += 1
                wordLength -= 1
            res.append(word)
            word, wordLength = '', ''
        return res
            



                




