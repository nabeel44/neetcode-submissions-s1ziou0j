class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted([ (position[i], speed[i]) for i in range(len(position))], reverse=True)
        for pair in pairs:
            arrival = (target - pair[0]) / pair[1]
            if stack:
                if arrival > stack[-1]:
                    stack.append(arrival)
            else: 
                stack.append(arrival)
        return len(stack)

        