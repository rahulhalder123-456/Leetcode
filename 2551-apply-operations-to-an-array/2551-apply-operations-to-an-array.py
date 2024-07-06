class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        write_index = 0

        # Apply the operations and shift non-zero elements to the front
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        
        # Move non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[write_index] = nums[i]
                write_index += 1
        
        # Fill the rest of the list with zeros
        for i in range(write_index, n):
            nums[i] = 0
        
        return nums