class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        index_map = defaultdict(list)
        
        # Create a dictionary where each key is a number from nums and the value is a list of indices where this number occurs
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        # Process each list of indices to calculate distances
        for indices in index_map.values():
            m = len(indices)
            if m == 1:
                continue  # No need to process if there is only one occurrence
            
            # Calculate prefix sums
            prefix_sum = [0] * (m + 1)
            for i in range(m):
                prefix_sum[i + 1] = prefix_sum[i] + indices[i]
            
            # Calculate distances using prefix sums
            for i in range(m):
                left_sum = prefix_sum[i]
                right_sum = prefix_sum[m] - prefix_sum[i + 1]
                arr[indices[i]] = indices[i] * i - left_sum + right_sum - indices[i] * (m - i - 1)
        
        return arr