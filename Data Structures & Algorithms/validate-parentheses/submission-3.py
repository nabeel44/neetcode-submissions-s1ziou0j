class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                complement = ''
                if char == ')':
                    complement = '('
                if char == '}':
                    complement = '{'
                if char == ']':
                    complement = '['
                top = stack.pop()
                if top != complement:
                    return False 
        return len(stack) == 0
        