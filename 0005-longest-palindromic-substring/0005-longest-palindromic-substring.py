class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            # Left and right nunchi expand chesi palindrome check chesthundi
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Oka sari unequal aithe loop apesthadi
            return s[left + 1:right]  # correct substring

        longest = ""

        for i in range(len(s)):
            # Odd length palindrome: single center (like 'aba')
            temp1 = expandAroundCenter(i, i)
            # Even length palindrome: double center (like 'abba')
            temp2 = expandAroundCenter(i, i + 1)

            # Longest ni update cheyyali
            if len(temp1) > len(longest):
                longest = temp1
            if len(temp2) > len(longest):
                longest = temp2

        return longest
