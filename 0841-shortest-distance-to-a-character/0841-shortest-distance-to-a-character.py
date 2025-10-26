class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [float('inf')] * n  # initialize with infinity
        
        # Left-to-right pass
        prev = float('-inf')  # no occurrence yet
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev
        
        # Right-to-left pass
        prev = float('inf')  # reset
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)
        
        return answer
