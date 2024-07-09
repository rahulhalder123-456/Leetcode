class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        
        full_multiplication = 1
        for num in nums:
            if num != 0:
                full_multiplication *= num

        result = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    result.append(full_multiplication)
                else:
                    result.append(0)
            else:
                result.append(full_multiplication // num)
        
        return result
           