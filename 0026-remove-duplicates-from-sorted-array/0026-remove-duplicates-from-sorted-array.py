class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1  # Index where we write the next unique element
        
        for i in range(1, len(nums)):
            if nums[i] != nums[write_index - 1]:
                if write_index != i:
                    nums[write_index] = nums[i]
                write_index += 1
        
        return write_index