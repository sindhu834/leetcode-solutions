class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)

        # Lists to store numbers based on remainder
        r1 = []
        r2 = []

        for x in nums:
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)

        r1.sort()
        r2.sort()

        if total % 3 == 0:
            return total
        
        elif total % 3 == 1:
            option1 = r1[0] if r1 else float('inf')
            option2 = r2[0] + r2[1] if len(r2) >= 2 else float('inf')
            return total - min(option1, option2)

        else:  # total % 3 == 2
            option1 = r2[0] if r2 else float('inf')
            option2 = r1[0] + r1[1] if len(r1) >= 2 else float('inf')
            return total - min(option1, option2)
