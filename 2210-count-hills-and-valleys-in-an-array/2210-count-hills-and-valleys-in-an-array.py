class Solution:
    def countHillValley(self, nums):
        count = 0
        n = len(nums)

        for i in range(1, n - 1):
            # skip duplicates
            if nums[i] == nums[i - 1]:
                continue

            # find closest non-equal left
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            # find closest non-equal right
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1

            if left >= 0 and right < n:
                # hill
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    count += 1
                # valley
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    count += 1

        return count
