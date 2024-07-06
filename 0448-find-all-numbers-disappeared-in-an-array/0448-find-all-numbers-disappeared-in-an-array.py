class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       # Mark each number present in the list by negating the value at its index
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # The indices of the positive numbers are the numbers that are missing
        missing_numbers = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
        return missing_numbers