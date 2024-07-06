class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # Dictionary to store the value and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []  # In case there is no solution, though the problem states there will be one
