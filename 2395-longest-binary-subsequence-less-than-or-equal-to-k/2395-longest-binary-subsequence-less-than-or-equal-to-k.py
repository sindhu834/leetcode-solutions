class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros = s.count('0')  # all zeros are safe
        value = 0
        power = 1
        ones = 0
        
        # traverse from right to left
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                if value + power <= k:
                    value += power
                    ones += 1
            power <<= 1  # multiply by 2
            if power > k:  # further left bits exceed limit
                break
        
        return zeros + ones
