class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        zeros = 0
        maxLen = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            # shrink window if zeros exceed k
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # update answer
            maxLen = max(maxLen, right - left + 1)

        return maxLen
