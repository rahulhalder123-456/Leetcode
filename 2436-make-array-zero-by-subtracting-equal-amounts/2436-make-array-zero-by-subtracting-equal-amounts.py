class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # count = 0
        # while any(nums):
        #     # Filter out non-zero numbers
        #     numbers = [num for num in nums if num != 0]
        #     if not numbers:
        #         break
            
        #     # Find the minimum non-zero number
        #     x = min(numbers)
            
        #     # Subtract the minimum value from all non-zero elements
        #     nums = [num - x if num != 0 else 0 for num in nums]
            
        #     count += 1
            
        # return count

        #Better process------------------------------------------------------
        # Use a set to track unique non-zero numbers
        unique_non_zero = set(num for num in nums if num != 0)
        
        # The number of operations needed is the number of unique non-zero elements
        return len(unique_non_zero)
