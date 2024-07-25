class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        num_set = set(nums)
        for num in range(0, max_num + 1):
            if num not in num_set:
                return num