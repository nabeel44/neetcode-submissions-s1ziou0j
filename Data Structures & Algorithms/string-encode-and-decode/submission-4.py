class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        say the length of the word, then a delimeter, then the word
        """
        res = ''
        for word in strs:
            length = len(word)
            res = res + str(length) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        wordLen = 0
        res = []
        while i < len(s):
            if wordLen == 0:
                newLen = ''
                while s[i] != '#':
                    newLen += s[i] 
                    i += 1

            i += 1
            wordLen = int(newLen)

            word = ''
            while wordLen > 0:
                word += s[i]
                i += 1
                wordLen -=1
            res.append(word)
        return res



