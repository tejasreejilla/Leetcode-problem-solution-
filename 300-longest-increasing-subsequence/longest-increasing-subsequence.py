class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            # Find the first index where tails[i] >= num
            left, right = 0, len(tails)

            while left < right:
                mid = (left + right) // 2

                if tails[mid] >= num:
                    right = mid
                else:
                    left = mid + 1

            # Replace the first value >= num
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)
