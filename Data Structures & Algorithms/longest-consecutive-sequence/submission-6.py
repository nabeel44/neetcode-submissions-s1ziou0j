class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get to the min and then go to the max
        if not nums:
            return 0
        nums = set(nums)
        seen = set()
        longest = 1
        for num in nums:
            if num - 1 not in nums:
                newLongest = 1
                while num + 1 in nums:
                    newLongest +=1 
                    num += 1
                if newLongest > longest:
                    longest = newLongest
        return longest
        

        