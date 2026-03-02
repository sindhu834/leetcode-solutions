class Solution:
    def minTime(self, skill, mana):
        n = len(skill)
        m = len(mana)
        
        # prefix sum of skills
        prefix = [0]*n
        prefix[0] = skill[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + skill[i]
        
        start = 0
        
        for j in range(m - 1):
            gap = 0
            
            for i in range(n):
                prev_prefix = prefix[i-1] if i > 0 else 0
                val = mana[j] * prefix[i] - mana[j+1] * prev_prefix
                gap = max(gap, val)
            
            start += gap
        
        # total time = finish time of last potion at last wizard
        total_time = start + mana[-1] * prefix[-1]
        return total_time