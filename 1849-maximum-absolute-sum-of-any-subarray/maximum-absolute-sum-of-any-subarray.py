class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        max_sum = 0
        min_sum = 0

        max_ending = 0
        min_ending = 0

        for num in nums:
            # Maximum subarray sum
            max_ending = max(0, max_ending + num)
            max_sum = max(max_sum, max_ending)

            # Minimum subarray sum
            min_ending = min(0, min_ending + num)
            min_sum = min(min_sum, min_ending)

        return max(max_sum, abs(min_sum))