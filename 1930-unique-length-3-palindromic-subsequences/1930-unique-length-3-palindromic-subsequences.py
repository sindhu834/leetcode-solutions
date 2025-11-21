class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first = {}
        last = {}

        # Track first and last positions
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = 0

        # Check for each character as the outer char (x)
        for ch in first:
            l = first[ch]
            r = last[ch]

            if l < r:  # Valid window
                middle_chars = set(s[l+1 : r])  # all chars between
                ans += len(middle_chars)

        return ans
