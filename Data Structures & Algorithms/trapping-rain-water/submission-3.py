class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = height[0], height[len(height) -1]
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            if leftMax >= rightMax:
                r -= 1
                volume = min(leftMax, rightMax) - height[r]
                if volume > 0:
                    area += volume
                if height[r] > rightMax:
                    rightMax = height[r]
            else:
                l += 1
                volume = min(leftMax, rightMax) - height[l]
                if volume > 0:
                    area += volume
                if height[l] > leftMax:
                    leftMax = height[l]
        return area
