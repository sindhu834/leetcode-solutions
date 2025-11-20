class Solution:
    def intersectionSizeTwo(self, intervals):
        # sort by end ascending, start descending (important!)
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # p1 < p2 are the two most recently chosen distinct points
        p1 = p2 = -10**18
        ans = 0
        
        for s, e in intervals:
            # how many of p1, p2 lie inside [s, e]
            cnt = 0
            if p1 >= s and p1 <= e: cnt += 1
            if p2 >= s and p2 <= e: cnt += 1
            
            if cnt == 2:
                continue
            elif cnt == 1:
                # need one more point: place it at e
                ans += 1
                p1, p2 = p2, e
            else:  # cnt == 0
                # need two points: place e-1 and e
                ans += 2
                p1, p2 = e - 1, e
        
        return ans
