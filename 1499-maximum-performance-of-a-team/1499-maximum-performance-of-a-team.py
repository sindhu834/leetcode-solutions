import heapq

class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Pair engineers (efficiency, speed) and sort by efficiency (descending)
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        speed_heap = []  # Min-heap for speeds
        total_speed = 0
        max_perf = 0
        
        # Step 2: Iterate engineers (highest efficiency first)
        for eff, spd in engineers:
            # If heap already has k engineers, remove the smallest speed
            if len(speed_heap) == k:
                total_speed -= heapq.heappop(speed_heap)
            
            # Add the new engineer
            heapq.heappush(speed_heap, spd)
            total_speed += spd
            
            # Step 3: Calculate performance = total_speed * current_min_efficiency
            performance = total_speed * eff
            max_perf = max(max_perf, performance)
        
        return max_perf % MOD
