class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_number = max(nums)
        return nums.index(max_number)