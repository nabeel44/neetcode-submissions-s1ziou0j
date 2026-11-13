class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[nums[0]], nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        final = 0
        while nums[final] != nums[slow]:
            final = nums[final]
            slow = nums[slow]
        return nums[slow]