class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def func(nums, goal):
            if goal < 0:
                return 0

            Sum = 0
            cnt = 0
            left = 0

            for right in range(len(nums)):
                Sum += nums[right]

                while Sum > goal:
                    Sum -= nums[left]
                    left += 1

                cnt += (right - left + 1)

            return cnt

        return func(nums, goal) - func(nums, goal - 1)
