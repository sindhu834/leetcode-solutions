class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        # compute initial power for each city using sliding window of size 2r+1
        power = [0] * n
        window = 0
        window_size = 2 * r + 1

        # initialize first window (for i = 0's window center at 0: covers indices [0, r])
        # but easier: build window for i=0 covering [0, r]
        # We'll build window for i=0 as sum of stations[0 .. 0 + r]
        for i in range(min(n, r + 1)):
            window += stations[i]
        power[0] = window

        # now slide to compute power for i = 1..n-1
        for i in range(1, n):
            # remove left element that no longer in window (index i - r - 1)
            left_out = i - r - 1
            if left_out >= 0:
                window -= stations[left_out]
            # add new right element that enters window (index i + r)
            right_in = i + r
            if right_in < n:
                window += stations[right_in]
            power[i] = window

        # feasibility check: can we make every city have power >= x using at most k additions?
        def can(x):
            diff = [0] * (n + 1)  # diff array, diff[n] is safe sentinel
            add_sum = 0
            remaining = k
            for i in range(n):
                add_sum += diff[i]  # apply any scheduled removals at i
                curr = power[i] + add_sum
                if curr < x:
                    need = x - curr
                    remaining -= need
                    if remaining < 0:
                        return False
                    add_sum += need
                    # place these need stations at p = min(n-1, i + r)
                    p = min(n - 1, i + r)
                    end = min(n - 1, p + r)
                    diff[end + 1] -= need  # remove effect after end
            return True

        # binary search for best minimum power
        low, high = 0, sum(stations) + k  # safe upper bound
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
