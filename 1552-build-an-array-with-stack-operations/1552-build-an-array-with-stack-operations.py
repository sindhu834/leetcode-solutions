class Solution:
    def buildArray(self, target, n):
        ans = []
        curr = 1
        i = 0  # pointer for target

        while i < len(target):
            if curr == target[i]:
                ans.append("Push")
                i += 1
            else:
                ans.append("Push")
                ans.append("Pop")
            curr += 1

        return ans
