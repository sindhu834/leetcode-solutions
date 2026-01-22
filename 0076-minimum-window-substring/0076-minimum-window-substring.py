from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dict_t = Counter(t)  # count of all chars in t
        required = len(dict_t)  # number of unique chars to satisfy
        left, right = 0, 0
        formed = 0  # how many unique chars satisfy their required frequency
        window_counts = {}
        ans = float("inf"), None, None  # window length, left, right

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Try and contract the window
            while left <= right and formed == required:
                char = s[left]

                # Update the answer
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Remove the leftmost char from window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
