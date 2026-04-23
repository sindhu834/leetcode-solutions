from collections import defaultdict

class Solution:
    def distance(self, nums):
        pos = defaultdict(list)

        # store indices for each number
        for i, num in enumerate(nums):
            pos[num].append(i)

        ans = [0] * len(nums)

        # process each group of same numbers
        for indices in pos.values():
            n = len(indices)

            # prefix sums of indices
            prefix = [0] * (n + 1)

            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]

            for i in range(n):
                idx = indices[i]

                # left side contribution
                left = idx * i - prefix[i]

                # right side contribution
                right = (prefix[n] - prefix[i + 1]) - idx * (n - i - 1)

                ans[idx] = left + right

        return ans