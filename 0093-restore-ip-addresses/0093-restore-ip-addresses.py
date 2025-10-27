class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, parts):
            # If 4 parts are formed and all digits are used
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return

            # Try segments of length 1 to 3
            for length in range(1, 4):
                # Don't go beyond string
                if start + length > len(s):
                    break

                segment = s[start:start + length]

                # Skip if segment starts with 0 and has more than one digit
                if segment.startswith('0') and len(segment) > 1:
                    continue

                # Convert to integer
                if int(segment) > 255:
                    continue

                # Recurse
                backtrack(start + length, parts + [segment])

        backtrack(0, [])
        return res
