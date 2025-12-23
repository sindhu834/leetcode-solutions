class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = 0
        for num in nums:
            max_or |= num

        self.count = 0
        n = len(nums)

        def dfs(index, curr_or):
            if index == n:
                if curr_or == max_or:
                    self.count += 1
                return

            # include nums[index]
            dfs(index + 1, curr_or | nums[index])

            # exclude nums[index]
            dfs(index + 1, curr_or)

        dfs(0, 0)
        return self.count
