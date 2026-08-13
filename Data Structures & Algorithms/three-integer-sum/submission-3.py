class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        if the number > 0 then we can break
        when you find a match, make sure the new left pointer is not on the same number
        when you find a match, keep going, don't return.
        """

        nums = sorted(nums)
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                continue
            if nums[i] == nums[i-1] and i > 0:
                continue
            target = -num
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                if total < target:
                    l += 1
                if total == target:
                     res.append([num, nums[l], nums[r]])
                     l += 1
                     r -= 1
                     while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
                


                 
