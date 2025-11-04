from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]
            count = Counter(sub)

            # Sort by frequency (descending), then by value (descending)
            sorted_items = sorted(count.items(), key=lambda item: (-item[1], -item[0]))

            # Take top x elements
            top_x = [num for num, freq in sorted_items[:x]]

            # Calculate sum of only those elements
            total = sum(val for val in sub if val in top_x)
            ans.append(total)

        return ans
