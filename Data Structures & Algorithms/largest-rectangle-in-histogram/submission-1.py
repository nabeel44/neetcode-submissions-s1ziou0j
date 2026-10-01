class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                curr = stack.pop()
                l = stack[-1] if stack else -1
                width = i - l - 1
                newArea = width * heights[curr]
                area = newArea if newArea > area else area
            stack.append(i)
        while stack:
            curr = stack.pop()
            if stack: 
                l = stack[-1]
            else:
                l = -1
            width = len(heights) - l - 1
            newArea = width * heights[curr]
            if newArea > area:
                area = newArea
        return area



        
        