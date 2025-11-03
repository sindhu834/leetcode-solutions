class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        n = len(colors)
        
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                # Add the smaller time to total
                total_time += min(neededTime[i], neededTime[i - 1])
                
                # Keep the one with greater neededTime
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        
        return total_time
