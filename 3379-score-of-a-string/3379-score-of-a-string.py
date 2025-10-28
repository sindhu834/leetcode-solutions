class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        for i in range(len(s)-1):
            a=ord(s[i])
            b=ord(s[i+1])
            temp= abs(a-b)
            ans= ans + temp
        
        return ans
        