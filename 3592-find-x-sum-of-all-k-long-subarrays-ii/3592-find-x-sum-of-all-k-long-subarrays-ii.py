from collections import Counter
import heapq

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        if k == 0:
            return []
        freq = Counter()

        # top_heap: min-heap of (freq, value) for elements currently in top_set
        top_heap = []
        # rest_heap: max-heap via negatives for elements not in top_set
        rest_heap = []

        top_set = set()   # elements currently in top x
        sum_top = 0       # sum of freq[val] * val for elements in top_set

        def push_top(f, v):
            heapq.heappush(top_heap, (f, v))
            top_set.add(v)

        def push_rest(f, v):
            heapq.heappush(rest_heap, (-f, -v))

        def pop_stale_top():
            # Ensure top_heap root is valid (in top_set and matches current freq)
            while top_heap:
                f, v = top_heap[0]
                if v in top_set and freq.get(v, 0) == f:
                    return (f, v)
                heapq.heappop(top_heap)
            return None

        def pop_stale_rest():
            # Ensure rest_heap root is valid (not in top_set and matches current freq)
            while rest_heap:
                fneg, vneg = rest_heap[0]
                f, v = -fneg, -vneg
                if v not in top_set and freq.get(v, 0) == f:
                    return (f, v)
                heapq.heappop(rest_heap)
            return None

        def promote_best_from_rest():
            nonlocal sum_top
            while len(top_set) < x:
                best = pop_stale_rest()
                if not best:
                    break
                f, v = best
                # remove from rest heap (we know it's at root)
                heapq.heappop(rest_heap)
                push_top(f, v)
                sum_top += f * v

        def try_swap():
            # Swap best rest with worst top if rest better
            nonlocal sum_top
            while True:
                best_rest = pop_stale_rest()
                worst_top = pop_stale_top()
                if not best_rest or not worst_top:
                    return
                fR, vR = best_rest
                fT, vT = worst_top
                # rest is better if freq bigger or same freq and value bigger
                if (fR > fT) or (fR == fT and vR > vT):
                    # pop both heaps (they are at roots)
                    heapq.heappop(rest_heap)
                    heapq.heappop(top_heap)
                    # move worst_top to rest
                    top_set.remove(vT)
                    sum_top -= fT * vT
                    push_rest(fT, vT)
                    # move best_rest to top
                    push_top(fR, vR)
                    sum_top += fR * vR
                    # continue loop to check if more swaps needed
                else:
                    return

        # function to update frequency of value `v` from old to new
        def freq_update(v, delta):
            # delta = +1 (add) or -1 (remove)
            old = freq.get(v, 0)
            new = old + delta
            if new < 0:
                new = 0
            freq[v] = new
            if new == 0:
                # if it was in top_set, remove its contribution
                if v in top_set:
                    # lazy removal: mark removed; actual heap entries cleaned on pop
                    top_set.remove(v)
                    # remove contribution of old occurrences
                    # old is the previous frequency
                    nonlocal_sum_adjust = old * v
                    # But we cannot modify sum_top via nested assignment; do below
                # we can't directly remove from rest heap; lazy deletion will handle
            # push the updated entry into appropriate heap (lazy)
            if v in top_set:
                # it remains or will be rechecked; push updated freq into top_heap
                if new > 0:
                    heapq.heappush(top_heap, (new, v))
                else:
                    # new == 0: it was in top_set and became 0: we already removed from top_set above,
                    # but there may be stale heap entries
                    pass
            else:
                if new > 0:
                    heapq.heappush(rest_heap, (-new, -v))
                else:
                    # new==0: nothing to push
                    pass

        # The nested function above attempted to modify sum_top via closure which is messy.
        # Instead implement a direct update process inline below for correctness.

        # We'll re-implement updates inline so sum_top updates correctly.

        # Reset everything and implement sliding window with correct updates:
        freq.clear()
        top_heap.clear()
        rest_heap.clear()
        top_set.clear()
        sum_top = 0
        res = []

        # helper inline update that performs the full maintenance when an element's freq changes
        def apply_change(v, delta):
            nonlocal sum_top
            old = freq.get(v, 0)
            new = old + delta
            if new < 0:
                new = 0
            # update freq map
            if new == 0:
                if v in freq:
                    del freq[v]
            else:
                freq[v] = new

            # If v was in top_set before change:
            was_in_top = (v in top_set)
            if was_in_top:
                # remove previous contribution (old * v)
                sum_top -= old * v
                # if new == 0: remove from top_set immediately
                if new == 0:
                    top_set.remove(v)
                    # we don't push anything for v
                else:
                    # push updated entry into top_heap (lazy)
                    heapq.heappush(top_heap, (new, v))
                    top_set.add(v)  # ensure present (it already was)
                    sum_top += new * v
            else:
                # not in top_set before
                if new == 0:
                    # nothing to add
                    pass
                else:
                    # push updated into rest heap
                    heapq.heappush(rest_heap, (-new, -v))

            # Now rebalance: ensure top_set size <= x and contains best elements
            # 1) promote until top_set size == min(x, distinct_count)
            promote_best_from_rest()
            # 2) swap while best rest is better than worst top
            try_swap()

        # Build initial window
        for i in range(k if k <= n else n):
            v = nums[i]
            apply_change(v, +1)

        if n >= k:
            res.append(sum_top)

        # Slide
        for i in range(k, n):
            # add nums[i], remove nums[i-k]
            addv = nums[i]
            delv = nums[i - k]
            apply_change(addv, +1)
            apply_change(delv, -1)
            res.append(sum_top)

        return res
