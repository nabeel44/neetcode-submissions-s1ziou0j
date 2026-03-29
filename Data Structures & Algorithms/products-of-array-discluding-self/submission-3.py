class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ 
        pass through once L -> R
        [1, 1, 2, 8]
        multiply this list by the pass through R -> L (decreasing list)
        [48, 24, 12, 8]
        """
        total = 1
        res = []
        for i in range(len(nums)):
            res.append(total)
            total *= nums[i]
        
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= total
            total *= nums[i]
        
        return res





