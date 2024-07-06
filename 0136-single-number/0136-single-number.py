class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # seen = set()
        # duplicate = set()
        # for num in nums:
        #     if num in seen:
        #         duplicate.add(num)
        #     else:
        #         seen.add(num)
        # for num in nums:
        #     if num not in duplicate:
        #         return num
        single = 0
        for num in nums:
            single ^= num
        return single