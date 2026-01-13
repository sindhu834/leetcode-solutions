class Solution:
    def diStringMatch(self, s: str):
        n = len(s)
        low, high = 0, n
        result = []

        for ch in s:
            if ch == 'I':
                result.append(low)
                low += 1
            else:  # 'D'
                result.append(high)
                high -= 1

        # append the last remaining number
        result.append(low)
        return result
