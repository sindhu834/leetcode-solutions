class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stack = []
        ans = 0
        for x in nums:
            # x == 0 splits segments: clear stack
            if x == 0:
                stack.clear()
                continue

            # remove all larger layers (they end before current x)
            while stack and stack[-1] > x:
                stack.pop()

            # if current value starts a new layer, count it and push
            if not stack or stack[-1] < x:
                stack.append(x)
                ans += 1
            # if stack[-1] == x -> same layer continues, do nothing

        return ans
