class Solution:
    def movesToStamp(self, stamp: str, target: str):
        m, n = len(stamp), len(target)
        t = list(target)
        res = []
        changed = True

        def can_stamp(i):
            changed_local = False
            for j in range(m):
                if t[i + j] == '?':
                    continue
                if t[i + j] != stamp[j]:
                    return False
                changed_local = True
            return changed_local

        def do_stamp(i):
            for j in range(m):
                t[i + j] = '?'

        while changed:
            changed = False
            for i in range(n - m + 1):
                if can_stamp(i):
                    do_stamp(i)
                    res.append(i)
                    changed = True

        # check if fully stamped
        if all(c == '?' for c in t):
            return res[::-1]
        return []
