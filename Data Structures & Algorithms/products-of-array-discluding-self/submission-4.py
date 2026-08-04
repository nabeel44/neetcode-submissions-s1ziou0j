class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        the product at a point is the product of everything on its left and its right
        pass through and every number is the 

        1, 1, 2, 8
        1, 6, 24, 48
        48, 24, 12, 8
        """
        res = [1] * len(nums)
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            if i == 0:
                prefix *= nums[i]
                continue
            else:
                res[i] = prefix
                prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                postfix *= nums[i]
                continue
            else:
                res[i] *= postfix
                postfix *= nums[i]
        return res
            

                
                
            

        
        