class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        import bisect

        n2 = len(nums2)

        # helper: count number of pairs (a in nums1, b in nums2) with a*b <= x
        def count_leq(x):
            cnt = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        cnt += n2
                elif a > 0:
                    # want b <= floor(x / a)
                    t = x // a
                    cnt += bisect.bisect_right(nums2, t)
                else:  # a < 0
                    # want b >= ceil(x / a)
                    # compute ceil(x/a) in integer arithmetic safely:
                    # ceil(x/a) == -((-x) // a)
                    thresh = -((-x) // a)
                    # number of b >= thresh
                    j = bisect.bisect_left(nums2, thresh)
                    cnt += n2 - j
            return cnt

        # search bounds: products between -1e10..1e10 safe given constraints
        lo, hi = -10**10, 10**10
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
