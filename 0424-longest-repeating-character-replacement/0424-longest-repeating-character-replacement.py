class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "AAABBCCD" K = 2 
        n = len(s) 
        left,right = 0,0 
        maxLen = 0 
        maxFreq = 0  
        mpp = [0]*26  # O(1)
        while(right<n):  
            mpp[ord(s[right])-ord('A')]+=1    
            maxFreq = max(maxFreq,mpp[ord(s[right])-ord('A')]) 
            # shrink  
            while(right-left+1 - maxFreq > k):   
                mpp[ord(s[left])-ord('A')]-=1
                left+=1     
            maxLen = max(maxLen,right-left+1) 
            right+=1 
        return maxLen
        