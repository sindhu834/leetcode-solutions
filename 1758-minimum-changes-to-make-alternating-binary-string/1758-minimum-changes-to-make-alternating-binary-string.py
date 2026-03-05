class Solution:
    def minOperations(self, s: str) -> int:
        change0 = 0  # pattern starting with '0'
        change1 = 0  # pattern starting with '1'
        
        for i in range(len(s)):
            
            # pattern: 010101
            if s[i] != ('0' if i % 2 == 0 else '1'):
                change0 += 1
            
            # pattern: 101010
            if s[i] != ('1' if i % 2 == 0 else '0'):
                change1 += 1
        
        return min(change0, change1)